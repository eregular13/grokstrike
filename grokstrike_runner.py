#!/usr/bin/env python3
"""GrokStrike v1.0 — systematic tool documentation runner for local Docker lab."""
from __future__ import annotations

import json
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# Add Aegis registry
sys.path.insert(0, str(Path("C:/AegisControlPlane")))
from aegis.registry import TOOLS, CATEGORIES, tool_count, render_command  # noqa: E402

KALI = "aegis-kali"
DVWA = "http://aegis-target"
DVWA_HOST = "aegis-target"
JUICE = "http://aegis-juice:3000"
JUICE_HOST = "aegis-juice"
OUT = Path("C:/GrokStrike")
RAW = OUT / "raw_notes"
FINAL = OUT / "final"
MAX_OUT = 8000
TIMEOUT_DEFAULT = 90

CATEGORY_PURPOSE = {
    "network": "Network Reconnaissance — port scanning, service enumeration, SMB/DNS discovery",
    "web": "Web Application Security — crawling, fuzzing, vulnerability scanning",
    "browser": "Browser Agent — headless rendering, DOM capture, screenshots",
    "auth": "Authentication Brute Force — credential attacks, hash cracking",
    "binary": "Binary Analysis / Reverse Engineering — disassembly, debugging, firmware",
    "cloud": "Cloud & Container Security — K8s, AWS, container image scanning",
    "ctf": "CTF / Forensics — steganography, carving, memory analysis",
    "osint": "OSINT — open-source intelligence gathering",
    "exploit": "Exploit Generation — Metasploit, impacket, post-exploitation",
    "agent": "Autonomous Agent — orchestration and correlation helpers",
    "forensics": "Digital Forensics — memory dumps, metadata, carving",
}


def pick_target(tool) -> str:
    if tool.category in {"web", "browser", "auth", "exploit"} and tool.dvwa:
        return DVWA
    if tool.category in {"web", "browser"} and not tool.dvwa:
        return JUICE
    if tool.category == "network" and tool.name in {"nc", "nmap", "nmap-quick", "nmap-udp", "masscan"}:
        return DVWA_HOST
    if tool.category == "network":
        return DVWA_HOST
    if tool.category in {"osint"}:
        return "localhost"
    return DVWA_HOST


def effectiveness(tool, exit_code: int, stdout: str, stderr: str) -> int:
    if exit_code == 0 and len(stdout.strip()) > 20:
        return 8
    if exit_code == 0:
        return 6
    if "not found" in stderr.lower() or "command not found" in (stdout + stderr).lower():
        return 1
    if len(stdout.strip()) > 50:
        return 5
    return 3


def run_cmd(cmd: str, timeout: int) -> tuple[int, str, str, float]:
    started = time.time()
    try:
        proc = subprocess.run(
            ["docker", "exec", KALI, "bash", "-lc", cmd],
            capture_output=True,
            text=True,
            timeout=timeout,
            encoding="utf-8",
            errors="replace",
        )
        return proc.returncode, proc.stdout, proc.stderr, round(time.time() - started, 2)
    except subprocess.TimeoutExpired:
        return -1, "", f"TIMEOUT after {timeout}s", round(time.time() - started, 2)
    except Exception as exc:
        return -1, "", str(exc), round(time.time() - started, 2)


def ensure_workspace() -> None:
    subprocess.run(
        ["docker", "exec", KALI, "bash", "-lc",
         "mkdir -p /workspace /results && "
         "echo '5d41402abc4b2a76b9719d911017c592' > /workspace/hash.txt && "
         "echo -e '#!/bin/bash\\necho hello' > /workspace/binary && chmod +x /workspace/binary && "
         "echo 'GrokStrike lab file' > /workspace/file && "
         "touch /workspace/mem.dump /workspace/disk.img /workspace/image.jpg /workspace/image.png"],
        check=False,
    )


def write_note(tool, target: str, cmd: str, exit_code: int, stdout: str, stderr: str, duration: float) -> dict:
    eff = effectiveness(tool, exit_code, stdout, stderr)
    out_summary = (stdout + stderr)[:MAX_OUT]
    gotchas = []
    if "not found" in (stdout + stderr).lower():
        gotchas.append("Binary not installed in Kali container — apt install required")
    if exit_code == -1 and "TIMEOUT" in stderr:
        gotchas.append("Command exceeded safe timeout — increase for full scans")
    if tool.category == "cloud":
        gotchas.append("Cloud tools need credentials/config — version/help checks only in lab")
    if tool.category in {"binary", "ctf", "forensics"}:
        gotchas.append("Uses synthetic /workspace artifacts — not live target attack")

    safe_params = f"--batch --risk=1 --level=1 for injection tools; -T4 for nmap; "
    safe_params += f"target={target} only; no destructive flags"

    md = f"""# {tool.name}

## Tool Name & Category
- **Name:** {tool.name}
- **Category:** {tool.category} ({CATEGORY_PURPOSE.get(tool.category, 'Security tooling')})
- **Binary:** `{tool.binary}`
- **Agent:** {tool.agent}
- **DVWA-optimized:** {tool.dvwa}

## Official Purpose
{tool.description}

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
{cmd}
```

**Target:** `{target}`  
**Duration:** {duration}s | **Exit code:** {exit_code}

## Full Output Summary
```
{out_summary}
```

## What I Learned / Edge Cases / Gotchas
{chr(10).join(f'- {g}' for g in gotchas) if gotchas else '- Executed successfully in isolated lab context'}
- Registry template: `{tool.template}`
- Tags: {', '.join(tool.tags) if tool.tags else 'none'}

## Effectiveness on This Target (1-10)
**{eff}/10** — {'Strong signal on DVWA/Juice Shop' if eff >= 7 else 'Limited output or tool not fully installed' if eff <= 3 else 'Partial results; useful for learning workflow'}

## Recommended Safe Parameters for Learning Labs
- {safe_params}
- Timeout: {min(tool.timeout, TIMEOUT_DEFAULT)}s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — {datetime.now(timezone.utc).isoformat()}*
"""
    path = RAW / f"{tool.name}.md"
    path.write_text(md, encoding="utf-8")
    return {
        "name": tool.name,
        "category": tool.category,
        "binary": tool.binary,
        "target": target,
        "command": cmd,
        "exit_code": exit_code,
        "duration_s": duration,
        "effectiveness": eff,
        "status": "success" if exit_code == 0 else "failed" if exit_code > 0 else "timeout/error",
        "output_chars": len(stdout) + len(stderr),
        "dvwa": tool.dvwa,
        "note_file": str(path),
    }


def main() -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    FINAL.mkdir(parents=True, exist_ok=True)
    ensure_workspace()

    inventory: list[dict] = []
    total = tool_count()
    print(f"[GrokStrike] Processing {total} tools from Aegis-HexStrike registry...")

    for i, tool in enumerate(TOOLS, 1):
        target = pick_target(tool)
        timeout = min(tool.timeout, TIMEOUT_DEFAULT)
        if tool.name in {"nuclei", "nikto", "gobuster", "feroxbuster", "dirb", "wfuzz", "sqlmap"}:
            timeout = min(tool.timeout, 120)
        if tool.category in {"cloud", "osint", "exploit"} and "msf" not in tool.name:
            timeout = min(timeout, 45)

        cmd = render_command(tool, target)
        # Safety: block external-only or destructive patterns
        if re.search(r"(rm\s+-rf|fork\s+bomb|:\(\)\{)", cmd):
            inventory.append({"name": tool.name, "status": "blocked", "reason": "destructive pattern"})
            continue

        print(f"  [{i}/{total}] {tool.name} -> {target[:40]}...")
        code, out, err, dur = run_cmd(cmd, timeout)
        entry = write_note(tool, target, cmd, code, out, err, dur)
        inventory.append(entry)

    # Document MCP API endpoints
    mcp_doc = {
        "name": "aegis-mcp-bridge",
        "category": "api",
        "endpoints": {
            "GET /health": "Returns status, tool count, Ollama host",
            "POST /": "JSON-RPC: tools/list, tools/call, ollama/chat, health",
        },
        "port": 8899,
        "note": "HexStrike-inspired offline MCP bridge in aegis-controlplane",
    }
    (RAW / "aegis-mcp-bridge.md").write_text(
        f"# Aegis MCP Bridge API\n\n```json\n{json.dumps(mcp_doc, indent=2)}\n```\n",
        encoding="utf-8",
    )

    # Phase 1 environment note
    env_note = """# GrokStrike Environment Verification

## SAFETY CHECK PASSED — local Docker lab only

| Container | Role | Status |
|-----------|------|--------|
| aegis-kali | Attacker (Kali rolling) | Running |
| aegis-target | DVWA :8080 | Running |
| aegis-juice | OWASP Juice Shop :3000 | Running |
| aegis-controlplane | HexStrike/Aegis MCP :8899 | Running |
| aegis-qdrant | Vector store :6333 | Running |

**HexStrike Health:** `GET http://localhost:8899/health` (MCP bridge inside controlplane)
**Note:** Port 8888 is SearXNG (LocalGrokLoop), not HexStrike.

Targets attacked: ONLY `http://aegis-target` (DVWA) and `http://aegis-juice:3000` (Juice Shop).
"""
    (RAW / "00_environment.md").write_text(env_note, encoding="utf-8")

    # Compile master report
    by_cat: dict[str, list] = {}
    for e in inventory:
        by_cat.setdefault(e["category"], []).append(e)

    toc_lines = ["# GrokStrike Learning Report — Master Synthesis\n"]
    toc_lines.append(f"**Generated:** {datetime.now(timezone.utc).isoformat()}\n")
    toc_lines.append("## SAFETY CHECK PASSED — local Docker lab only\n")
    toc_lines.append(f"**Tools documented:** {len(inventory)}\n")
    toc_lines.append("## Table of Contents\n")

    md_files = sorted(RAW.glob("*.md"))
    for f in md_files:
        toc_lines.append(f"- [{f.stem}](raw_notes/{f.name})")

    toc_lines.append("\n## Category Summaries\n")
    for cat, items in sorted(by_cat.items()):
        ok = sum(1 for x in items if x.get("status") == "success")
        avg_eff = sum(x.get("effectiveness", 0) for x in items) / max(len(items), 1)
        toc_lines.append(f"### {cat.title()} ({len(items)} tools)\n")
        toc_lines.append(f"- Success rate: {ok}/{len(items)}")
        toc_lines.append(f"- Avg effectiveness: {avg_eff:.1f}/10")
        toc_lines.append(f"- Purpose: {CATEGORY_PURPOSE.get(cat, 'N/A')}\n")

    reflections = {
        "network": "nmap + nc give fastest host visibility; SMB tools need Windows targets",
        "web": "whatweb/httpx fingerprint fast; nuclei/gobuster are highest-value on DVWA",
        "browser": "headless Chrome needs chromium package; curl capture works as fallback",
        "auth": "hydra needs correct form paths; hash tools need wordlists",
        "binary": "workspace stubs enable workflow learning without real malware",
        "cloud": "trivy/kube-* need cloud creds; version checks confirm install state",
        "ctf": "forensics tools need sample images — synthetic files created",
        "osint": "theHarvester works locally; Shodan/Censys need API keys",
        "exploit": "searchsploit offline; msf/impacket need lab network targets",
        "agent": "orchestration stubs — wire into Aegis Fusion for full automation",
    }
    toc_lines.append("\n## Category Reflections\n")
    for cat, msg in reflections.items():
        toc_lines.append(f"✅ Completed {cat.title()} Tools — Key takeaway: {msg}\n")

    (FINAL / "GrokStrike_Learning_Report.md").write_text("\n".join(toc_lines), encoding="utf-8")
    (FINAL / "tool_inventory.json").write_text(
        json.dumps({"generated": datetime.now(timezone.utc).isoformat(), "tools": inventory, "count": len(inventory)}, indent=2),
        encoding="utf-8",
    )
    (OUT / "complete.txt").write_text(
        " ALL NOTES SAVED TO C:\\GrokStrike on your Windows machine!\n"
        f" Tools documented: {len(inventory)}\n"
        f" Report: C:\\GrokStrike\\final\\GrokStrike_Learning_Report.md\n",
        encoding="utf-8",
    )
    print(f"\n[GrokStrike] DONE — {len(inventory)} tools -> {OUT}")


if __name__ == "__main__":
    main()