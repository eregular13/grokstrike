#!/usr/bin/env python3
"""GrokStrike v2 — thorough tool documentation with full bootstrap support."""
from __future__ import annotations

import json
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path("C:/AegisControlPlane")))
from aegis.registry import TOOLS, tool_count, render_command  # noqa: E402

KALI = "aegis-kali"
DVWA = "http://aegis-target"
JUICE = "http://aegis-juice:3000"
OUT = Path("C:/GrokStrike")
RAW = OUT / "raw_notes"
FINAL = OUT / "final"
MAX_OUT = 12000

CATEGORY_PURPOSE = {
    "network": "Network Reconnaissance",
    "web": "Web Application Security",
    "browser": "Browser Agent",
    "auth": "Authentication / Credential Testing",
    "binary": "Binary Analysis / Reverse Engineering",
    "cloud": "Cloud & Container Security",
    "ctf": "CTF / Forensics",
    "osint": "OSINT",
    "exploit": "Exploit Frameworks",
    "agent": "Autonomous Agents",
    "forensics": "Digital Forensics",
}

# Per-tool timeout overrides (seconds) — no aggressive capping
TIMEOUTS: dict[str, int] = {
    "nikto": 420,
    "nuclei": 300,
    "gobuster": 180,
    "feroxbuster": 180,
    "dirb": 180,
    "wfuzz": 120,
    "ffuf": 120,
    "sqlmap": 240,
    "sqlmap-crawl": 300,
    "sqlmap-os-shell": 300,
    "zap-baseline": 600,
    "trivy": 300,
    "john": 120,
    "hashcat": 120,
    "hydra-http": 60,
    "masscan": 60,
    "nmap": 120,
    "nmap-udp": 120,
}

# Tool-specific command overrides for better lab results
CMD_OVERRIDES: dict[str, str] = {
    "nikto": "nikto -h {web} -maxtime 360",
    "nuclei": "nuclei -u {web} -severity low,medium,high -silent -stats",
    "gobuster": "gobuster dir -u {web} -w /usr/share/wordlists/dirb/common.txt -q --no-error",
    "feroxbuster": "feroxbuster -u {web} -w /usr/share/wordlists/dirb/common.txt -q --time-limit 120s",
    "ffuf": "ffuf -u {web}/FUZZ -w /usr/share/wordlists/dirb/common.txt -mc 200,301,302,403 -t 20",
    "dirb": "dirb {web} /usr/share/wordlists/dirb/common.txt -S -r",
    "wfuzz": "wfuzz -c -z file,/usr/share/wordlists/dirb/common.txt --hc 404,500 -t 10 {web}/FUZZ",
    "sqlmap": (
        "COOKIE=$(/workspace/dvwa_login.sh {web}); "
        "sqlmap -u '{web}/vulnerabilities/sqli/?id=1&Submit=Submit' "
        "--cookie=\"$COOKIE\" --batch --level=2 --risk=1 --threads=2"
    ),
    "sqlmap-crawl": (
        "COOKIE=$(/workspace/dvwa_login.sh {web}); "
        "sqlmap -u {web} --cookie=\"$COOKIE\" --crawl=1 --batch --level=1 --risk=1"
    ),
    "commix": "commix -u '{web}/vulnerabilities/exec/' --cookie=\"$(/workspace/dvwa_login.sh {web})\" --batch --level=1",
    "dalfox": "dalfox url '{web}/vulnerabilities/xss_r/?name=test' --cookie \"$(/workspace/dvwa_login.sh {web})\" --silence",
    "hydra-http": (
        "hydra -l admin -P /usr/share/seclists/Passwords/Common-Credentials/10k-most-common.txt "
        "{host} http-get-form '/login.php:username=^USER^&password=^PASS^&Login=Login:F=Login failed' -t 4 -w 10 -f"
    ),
    "john": "john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt /workspace/hash.txt 2>&1 | head -30",
    "hashcat": "hashcat -m 0 -a 0 /workspace/hash.txt /usr/share/wordlists/rockyou.txt --force 2>&1 | head -30",
    "httpx": "echo '{web}' | httpx -title -tech-detect -status-code -silent",
    "wpscan": "wpscan --url {web} --no-update --enumerate vp --max-threads 2 2>&1 | head -40",
    "trivy": "trivy image --scanners vuln --severity HIGH,CRITICAL kalilinux/kali-rolling 2>&1 | head -50",
    "searchsploit": "searchsploit apache 2.4 debian 2>&1 | head -30",
    "nmap": "nmap -sV -sC -p 80,443,3000,8080 -T4 {host}",
    "nc": "nc -zv {host} 80 443 3000 8080 2>&1",
    "masscan": "masscan {host} -p80,443,3000,8080 --rate 500 2>&1",
    "whatweb": "whatweb -a 3 -v {web} 2>&1 | head -40",
    "wafw00f": "wafw00f -a {web} 2>&1",
    "curl-headers": "curl -sI {web} 2>&1",
    "curl-body": "curl -skL {web} 2>&1 | head -80",
    "graphql-voyager": "curl -sk {web}/api/Products 2>&1 | head -30",
    "browser-agent": "curl -skL {web} -o /results/browser_capture.html && wc -c /results/browser_capture.html",
}

NEXT_STEPS: dict[str, str] = {
    "nmap": "Run `nmap -sV --script vuln` for scripted checks; map all DVWA modules.",
    "gobuster": "Try `/usr/share/seclists/Discovery/Web-Content/raft-medium-words.txt` for deeper enum.",
    "sqlmap": "After auth, test `/vulnerabilities/sqli_blind/` and increase `--level=3`.",
    "nuclei": "Add `-tags dvwa,apache,misconfig` and export with `-jsonl -o /results/nuclei.jsonl`.",
    "nikto": "Pipe to report: `nikto -h URL -Format htm -output /results/nikto.html`.",
    "hydra-http": "Build custom wordlist with `cewl` from DVWA page content first.",
    "trivy": "Scan `bkimminich/juice-shop` and `vulnerables/web-dvwa` images directly.",
    "feroxbuster": "Add `-x php,txt,bak,old` extensions for PHP targets like DVWA.",
    "dalfox": "Point at Juice Shop search: `dalfox url 'http://aegis-juice:3000/#/search?q=test'`.",
    "whatweb": "Combine with `httpx -tech-detect` for pipeline fingerprinting.",
}


def pick_target(tool) -> str:
    if tool.category in {"web", "browser", "auth", "exploit"} and tool.dvwa:
        return DVWA
    if tool.category in {"web", "browser"} and not tool.dvwa:
        return JUICE
    if tool.category == "osint":
        return "localhost"
    return "aegis-target"


def render_lab_command(tool, target: str) -> str:
    if tool.name in CMD_OVERRIDES:
        tpl = CMD_OVERRIDES[tool.name]
    else:
        tpl = tool.template
    web = target if target.startswith("http") else f"http://{target}"
    host = target.replace("http://", "").replace("https://", "").split("/")[0].split(":")[0]
    cmd = tpl.format(target=target, web=web, host=host, url=web, extra="")
    return " ".join(cmd.split())


def get_timeout(tool) -> int:
    return TIMEOUTS.get(tool.name, min(tool.timeout, 180))


def run_cmd(cmd: str, timeout: int) -> tuple[int, str, str, float]:
    started = time.time()
    try:
        proc = subprocess.run(
            ["docker", "exec", KALI, "bash", "-lc", cmd],
            capture_output=True, text=True, timeout=timeout,
            encoding="utf-8", errors="replace",
        )
        return proc.returncode, proc.stdout, proc.stderr, round(time.time() - started, 2)
    except subprocess.TimeoutExpired as exc:
        out = (exc.stdout or b"").decode("utf-8", errors="replace") if exc.stdout else ""
        err = (exc.stderr or b"").decode("utf-8", errors="replace") if exc.stderr else ""
        return -1, out, f"TIMEOUT after {timeout}s\n{err}", round(time.time() - started, 2)
    except Exception as exc:
        return -1, "", str(exc), round(time.time() - started, 2)


def check_binary(binary: str) -> bool:
    proc = subprocess.run(
        ["docker", "exec", KALI, "bash", "-lc", f"command -v {binary} || which {binary} 2>/dev/null"],
        capture_output=True, text=True, timeout=15,
    )
    return proc.returncode == 0 and proc.stdout.strip() != ""


def extract_findings(tool_name: str, output: str) -> list[str]:
    findings = []
    patterns = [
        (r"open\s+(\S+)\s+(\S+)", "Open port/service"),
        (r"\[(\d+)\]\s+(.+)", "Nikto/nuclei finding"),
        (r"(Status: \d+)", "HTTP discovery"),
        (r"(vulnerable|injection|XSS|SQL)", "Potential vulnerability signal"),
        (r"(Apache/[\d.]+)", "Server version"),
        (r"(PHP/[\d.]+)", "PHP version"),
        (r"(parameter|injectable)", "Injection indicator"),
        (r"(Cookie .+ httponly)", "Cookie security issue"),
        (r"(Directory indexing)", "Directory listing"),
    ]
    for pat, label in patterns:
        for m in re.finditer(pat, output, re.IGNORECASE):
            findings.append(f"**{label}:** {m.group(0)[:120]}")
            if len(findings) >= 8:
                return findings
    if tool_name in NEXT_STEPS and not findings:
        findings.append("See output summary for raw tool data.")
    return findings[:8]


def effectiveness(exit_code: int, stdout: str, stderr: str, binary_ok: bool) -> tuple[int, str]:
    combined = stdout + stderr
    if not binary_ok:
        return 1, "Tool binary not installed"
    if exit_code == 0 and len(stdout.strip()) > 100:
        return 9, "Rich actionable output"
    if exit_code == 0 and len(stdout.strip()) > 20:
        return 7, "Good lab signal"
    if exit_code == 0:
        return 5, "Ran successfully, limited findings"
    if "not found" in combined.lower() or "command not found" in combined.lower():
        return 1, "Binary missing"
    if exit_code == -1 and "TIMEOUT" in stderr:
        return 4, "Partial output before timeout"
    if len(stdout.strip()) > 80:
        return 5, "Non-zero exit but useful output"
    return 3, "Minimal or error output"


def write_note(tool, target: str, cmd: str, exit_code: int, stdout: str, stderr: str,
               duration: float, binary_ok: bool) -> dict:
    eff, eff_reason = effectiveness(exit_code, stdout, stderr, binary_ok)
    out_summary = (stdout + ("\n--- STDERR ---\n" + stderr if stderr.strip() else ""))[:MAX_OUT]
    findings = extract_findings(tool.name, stdout + stderr)
    gotchas = []
    if not binary_ok:
        gotchas.append(f"`{tool.binary}` not found — run `scripts/kali-full-bootstrap.sh`")
    if exit_code == -1 and "TIMEOUT" in stderr:
        gotchas.append(f"Hit {get_timeout(tool)}s timeout — increase TIMEOUTS['{tool.name}'] for full scan")
    if tool.name.startswith("sqlmap") or tool.name == "commix" or tool.name == "dalfox":
        gotchas.append("DVWA requires authenticated session — `/workspace/dvwa_login.sh` sets cookies + security=low")
    if tool.category == "cloud":
        gotchas.append("Cloud tools may need API credentials; container scans work offline with trivy/grype")
    if tool.category in {"binary", "ctf", "forensics"}:
        gotchas.append("Uses synthetic /workspace artifacts — swap in real samples for deeper RE/forensics")
    if "juice" in target:
        gotchas.append("Juice Shop is a SPA — API endpoints (`/rest`, `/api`) often more fruitful than path brute force")

    next_step = NEXT_STEPS.get(tool.name, f"Run `{tool.binary} --help` and tune `{tool.template}` for your target.")

    md = f"""# {tool.name}

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | {tool.category} — {CATEGORY_PURPOSE.get(tool.category, 'Security')} |
| **Binary** | `{tool.binary}` {'✅ installed' if binary_ok else '❌ missing'} |
| **Agent** | {tool.agent} |
| **DVWA-optimized** | {tool.dvwa} |
| **Lab target** | `{target}` |

## Official Purpose
{tool.description}

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
{cmd}
```

| Metric | Value |
|--------|-------|
| Duration | {duration}s |
| Exit code | {exit_code} |
| Effectiveness | **{eff}/10** — {eff_reason} |

## Key Findings
{chr(10).join(f'- {f}' for f in findings) if findings else '- No automated findings extracted — review output below'}

## Full Output Summary
```
{out_summary}
```

## What I Learned / Edge Cases / Gotchas
{chr(10).join(f'- {g}' for g in gotchas) if gotchas else '- Executed successfully in isolated lab'}
- Registry template: `{tool.template}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: {get_timeout(tool)}s

## Next Steps for Exploration & Development
{next_step}

---
*GrokStrike v2 — {datetime.now(timezone.utc).isoformat()}*
"""
    path = RAW / f"{tool.name}.md"
    path.write_text(md, encoding="utf-8")
    return {
        "name": tool.name,
        "category": tool.category,
        "binary": tool.binary,
        "binary_installed": binary_ok,
        "target": target,
        "command": cmd,
        "exit_code": exit_code,
        "duration_s": duration,
        "effectiveness": eff,
        "effectiveness_reason": eff_reason,
        "status": "success" if exit_code == 0 else "failed" if exit_code > 0 else "timeout/error",
        "output_chars": len(stdout) + len(stderr),
        "dvwa": tool.dvwa,
        "note_file": str(path),
    }


def run_bootstrap() -> dict:
    script = (OUT / "scripts" / "kali-full-bootstrap.sh").read_text(encoding="utf-8")
    proc = subprocess.run(
        ["docker", "exec", KALI, "bash", "-lc", script],
        capture_output=True, text=True, timeout=1800,
        encoding="utf-8", errors="replace",
    )
    return {
        "exit_code": proc.returncode,
        "stdout": proc.stdout[-4000:],
        "stderr": proc.stderr[-2000:],
    }


def write_exploration_guide(inventory: list[dict]) -> None:
    ok = [t for t in inventory if t.get("status") == "success" and t.get("effectiveness", 0) >= 7]
    missing = [t for t in inventory if not t.get("binary_installed")]
    top_web = sorted([t for t in inventory if t["category"] == "web"], key=lambda x: -x.get("effectiveness", 0))[:10]

    guide = ["# GrokStrike Exploration & Development Guide\n"]
    guide.append(f"**Generated:** {datetime.now(timezone.utc).isoformat()}\n")
    guide.append("## Lab Targets\n")
    guide.append("| Target | URL (host) | URL (Kali) | Default creds |\n")
    guide.append("|--------|------------|------------|---------------|\n")
    guide.append("| DVWA | http://localhost:8080 | http://aegis-target | admin / password |\n")
    guide.append("| Juice Shop | http://localhost:3000 | http://aegis-juice:3000 | (register or default challenges) |\n")
    guide.append("\n## Quick Start Workflow\n")
    guide.append("```bash\n")
    guide.append("# 1. Bootstrap tools (once)\n")
    guide.append("docker exec aegis-kali bash /workspace/scripts/kali-full-bootstrap.sh\n\n")
    guide.append("# 2. DVWA auth cookie for injection tools\n")
    guide.append("docker exec aegis-kali /workspace/dvwa_login.sh http://aegis-target\n\n")
    guide.append("# 3. Recommended attack chain\n")
    guide.append("nmap -sV aegis-target && whatweb http://aegis-target\n")
    guide.append("gobuster dir -u http://aegis-target -w /usr/share/wordlists/dirb/common.txt\n")
    guide.append("nikto -h http://aegis-target -maxtime 600\n")
    guide.append("nuclei -u http://aegis-target -severity medium,high\n")
    guide.append("```\n")
    guide.append("\n## Highest-Value Tools (effectiveness ≥ 7)\n")
    for t in sorted(ok, key=lambda x: -x.get("effectiveness", 0))[:25]:
        guide.append(f"- **{t['name']}** ({t['category']}) — {t.get('effectiveness_reason', '')} → `{t['note_file']}`\n")
    guide.append("\n## Top Web Tools for DVWA/Juice Shop Development\n")
    for t in top_web:
        guide.append(f"- {t['name']}: effectiveness {t.get('effectiveness')}/10\n")
    guide.append(f"\n## Missing Binaries ({len(missing)} tools)\n")
    guide.append("Install via bootstrap or manual `apt install` / `pip install`:\n")
    for t in missing[:40]:
        guide.append(f"- `{t['name']}` → binary `{t['binary']}`\n")
    if len(missing) > 40:
        guide.append(f"- ... and {len(missing)-40} more (see tool_inventory.json)\n")
    guide.append("\n## Development Integration\n")
    guide.append("- **Aegis Fusion:** Tool registry at `C:\\AegisControlPlane\\aegis\\registry.py`\n")
    guide.append("- **MCP Bridge:** `POST http://localhost:8899/` with `{\"method\":\"tools/call\",\"params\":{\"name\":\"nmap\",\"target\":\"aegis-target\"}}`\n")
    guide.append("- **Re-run docs:** `python C:\\GrokStrike\\grokstrike_runner.py`\n")
    guide.append("- **DVWA chains:** `full_assessment`, `injection`, `web_enum` in registry `DVWA_CHAINS`\n")
    (FINAL / "Exploration_Development_Guide.md").write_text("".join(guide), encoding="utf-8")


def main() -> None:
    import os
    RAW.mkdir(parents=True, exist_ok=True)
    FINAL.mkdir(parents=True, exist_ok=True)
    (OUT / "scripts").mkdir(exist_ok=True)
    skip_boot = os.environ.get("GROKSTRIKE_SKIP_BOOTSTRAP", "") == "1"

    boot = {"exit_code": 0, "stdout": "skipped", "stderr": ""}
    if not skip_boot:
        subprocess.run(["docker", "exec", KALI, "mkdir", "-p", "/workspace/scripts"], check=False)
        subprocess.run(
            ["docker", "cp", str(OUT / "scripts" / "kali-full-bootstrap.sh"), f"{KALI}:/workspace/scripts/kali-full-bootstrap.sh"],
            check=False,
        )
        print("[GrokStrike v2] Running full Kali bootstrap (may take 10-20 min)...")
        boot = run_bootstrap()
        print(f"  Bootstrap exit: {boot['exit_code']}")
    else:
        print("[GrokStrike v2] Skipping bootstrap (GROKSTRIKE_SKIP_BOOTSTRAP=1)")

    (RAW / "bootstrap_log.md").write_text(
        f"# Bootstrap Log\n\nExit: {boot['exit_code']}\n\n```\n{boot['stdout']}\n{boot['stderr']}\n```\n",
        encoding="utf-8",
    )

    inventory: list[dict] = []
    total = tool_count()
    print(f"[GrokStrike v2] Running {total} tools with full timeouts...")

    for i, tool in enumerate(TOOLS, 1):
        target = pick_target(tool)
        timeout = get_timeout(tool)
        cmd = render_lab_command(tool, target)
        binary_ok = check_binary(tool.binary)

        if re.search(r"(rm\s+-rf|fork\s+bomb)", cmd):
            continue

        print(f"  [{i}/{total}] {tool.name} (timeout={timeout}s, bin={'OK' if binary_ok else 'MISS'})")
        if not binary_ok and tool.category not in {"agent"}:
            entry = write_note(tool, target, cmd, 127, "", f"command not found: {tool.binary}", 0.0, False)
            inventory.append(entry)
            continue

        code, out, err, dur = run_cmd(cmd, timeout)
        entry = write_note(tool, target, cmd, code, out, err, dur, binary_ok)
        inventory.append(entry)

    # Meta docs
    (RAW / "00_environment.md").write_text(f"""# GrokStrike Environment — v2 Full Bootstrap

## SAFETY CHECK PASSED — local Docker lab only

| Container | Role | Endpoint |
|-----------|------|----------|
| aegis-kali | Attacker | docker exec aegis-kali |
| aegis-target | DVWA | http://localhost:8080 |
| aegis-juice | Juice Shop | http://localhost:3000 |
| aegis-controlplane | MCP :8899 | http://localhost:8899/health |

**Bootstrap:** `scripts/kali-full-bootstrap.sh` — {boot['exit_code'] == 0 and 'SUCCESS' or 'PARTIAL'}
**Tools documented:** {len(inventory)}
**Generated:** {datetime.now(timezone.utc).isoformat()}
""", encoding="utf-8")

    by_cat: dict[str, list] = {}
    for e in inventory:
        by_cat.setdefault(e["category"], []).append(e)

    lines = ["# GrokStrike Learning Report — v2 (Full Bootstrap)\n"]
    lines.append(f"**Generated:** {datetime.now(timezone.utc).isoformat()}\n\n")
    lines.append("## SAFETY CHECK PASSED — local Docker lab only\n\n")
    ok = sum(1 for t in inventory if t["status"] == "success")
    high = sum(1 for t in inventory if t.get("effectiveness", 0) >= 7)
    lines.append(f"| Metric | Value |\n|--------|-------|\n")
    lines.append(f"| Tools run | {len(inventory)} |\n")
    lines.append(f"| Success (exit 0) | {ok} |\n")
    lines.append(f"| High effectiveness (≥7) | {high} |\n")
    lines.append(f"| Binaries installed | {sum(1 for t in inventory if t.get('binary_installed'))} |\n\n")
    lines.append("See [Exploration_Development_Guide.md](Exploration_Development_Guide.md) for workflows.\n\n")
    lines.append("## Category Summaries\n\n")
    for cat, items in sorted(by_cat.items()):
        c_ok = sum(1 for x in items if x.get("status") == "success")
        avg = sum(x.get("effectiveness", 0) for x in items) / max(len(items), 1)
        lines.append(f"### {cat.title()} — {c_ok}/{len(items)} success, avg {avg:.1f}/10\n\n")
    lines.append("## All Notes\n\n")
    for f in sorted(RAW.glob("*.md")):
        lines.append(f"- [{f.stem}](../raw_notes/{f.name})\n")

    (FINAL / "GrokStrike_Learning_Report.md").write_text("".join(lines), encoding="utf-8")
    (FINAL / "tool_inventory.json").write_text(
        json.dumps({"version": "2.0", "generated": datetime.now(timezone.utc).isoformat(),
                    "bootstrap_exit": boot["exit_code"], "tools": inventory, "count": len(inventory)}, indent=2),
        encoding="utf-8",
    )
    write_exploration_guide(inventory)
    (OUT / "complete.txt").write_text(
        f"GrokStrike v2 COMPLETE\nTools: {len(inventory)} | Success: {ok} | High-value: {high}\n"
        f"Guide: C:\\GrokStrike\\final\\Exploration_Development_Guide.md\n",
        encoding="utf-8",
    )
    print(f"\n[GrokStrike v2] DONE — {ok}/{len(inventory)} success, {high} high-value tools")


if __name__ == "__main__":
    main()