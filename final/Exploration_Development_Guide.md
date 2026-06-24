# GrokStrike Exploration & Development Guide
**Generated:** 2026-06-24T05:48:54.932224+00:00
## Lab Targets
| Target | URL (host) | URL (Kali) | Default creds |
|--------|------------|------------|---------------|
| DVWA | http://localhost:8080 | http://aegis-target | admin / password |
| Juice Shop | http://localhost:3000 | http://aegis-juice:3000 | (register or default challenges) |

## Quick Start Workflow
```bash
# 1. Bootstrap tools (once)
docker exec aegis-kali bash /workspace/scripts/kali-full-bootstrap.sh

# 2. DVWA auth cookie for injection tools
docker exec aegis-kali /workspace/dvwa_login.sh http://aegis-target

# 3. Recommended attack chain
nmap -sV aegis-target && whatweb http://aegis-target
gobuster dir -u http://aegis-target -w /usr/share/wordlists/dirb/common.txt
nikto -h http://aegis-target -maxtime 600
nuclei -u http://aegis-target -severity medium,high
```

## Highest-Value Tools (effectiveness ≥ 7)
- **nmap** (network) — Rich actionable output → `C:\GrokStrike\raw_notes\nmap.md`
- **nmap-quick** (network) — Rich actionable output → `C:\GrokStrike\raw_notes\nmap-quick.md`
- **nmap-udp** (network) — Rich actionable output → `C:\GrokStrike\raw_notes\nmap-udp.md`
- **theharvester** (network) — Rich actionable output → `C:\GrokStrike\raw_notes\theharvester.md`
- **enum4linux-ng** (network) — Rich actionable output → `C:\GrokStrike\raw_notes\enum4linux-ng.md`
- **smbmap** (network) — Rich actionable output → `C:\GrokStrike\raw_notes\smbmap.md`
- **netexec** (network) — Rich actionable output → `C:\GrokStrike\raw_notes\netexec.md`
- **hping3** (network) — Rich actionable output → `C:\GrokStrike\raw_notes\hping3.md`
- **traceroute** (network) — Rich actionable output → `C:\GrokStrike\raw_notes\traceroute.md`
- **whois** (network) — Rich actionable output → `C:\GrokStrike\raw_notes\whois.md`
- **nc** (network) — Rich actionable output → `C:\GrokStrike\raw_notes\nc.md`
- **whatweb** (web) — Rich actionable output → `C:\GrokStrike\raw_notes\whatweb.md`
- **nikto** (web) — Rich actionable output → `C:\GrokStrike\raw_notes\nikto.md`
- **gobuster** (web) — Rich actionable output → `C:\GrokStrike\raw_notes\gobuster.md`
- **feroxbuster** (web) — Rich actionable output → `C:\GrokStrike\raw_notes\feroxbuster.md`
- **dirsearch** (web) — Rich actionable output → `C:\GrokStrike\raw_notes\dirsearch.md`
- **ffuf** (web) — Rich actionable output → `C:\GrokStrike\raw_notes\ffuf.md`
- **dirb** (web) — Rich actionable output → `C:\GrokStrike\raw_notes\dirb.md`
- **wfuzz** (web) — Rich actionable output → `C:\GrokStrike\raw_notes\wfuzz.md`
- **sqlmap** (web) — Rich actionable output → `C:\GrokStrike\raw_notes\sqlmap.md`
- **sqlmap-crawl** (web) — Rich actionable output → `C:\GrokStrike\raw_notes\sqlmap-crawl.md`
- **wafw00f** (web) — Rich actionable output → `C:\GrokStrike\raw_notes\wafw00f.md`
- **commix** (web) — Rich actionable output → `C:\GrokStrike\raw_notes\commix.md`
- **curl-headers** (web) — Rich actionable output → `C:\GrokStrike\raw_notes\curl-headers.md`
- **curl-body** (web) — Rich actionable output → `C:\GrokStrike\raw_notes\curl-body.md`

## Top Web Tools for DVWA/Juice Shop Development
- whatweb: effectiveness 9/10
- nikto: effectiveness 9/10
- gobuster: effectiveness 9/10
- feroxbuster: effectiveness 9/10
- dirsearch: effectiveness 9/10
- ffuf: effectiveness 9/10
- dirb: effectiveness 9/10
- wfuzz: effectiveness 9/10
- sqlmap: effectiveness 9/10
- sqlmap-crawl: effectiveness 9/10

## Missing Binaries (82 tools)
Install via bootstrap or manual `apt install` / `pip install`:
- `rustscan` → binary `rustscan`
- `autorecon` → binary `autorecon`
- `amass` → binary `amass`
- `wpscan` → binary `wpscan`
- `arjun` → binary `arjun`
- `paramspider` → binary `paramspider`
- `dalfox` → binary `dalfox`
- `sslyze` → binary `sslyze`
- `nosqlmap` → binary `nosqlmap`
- `tplmap` → binary `tplmap`
- `jwt-tool` → binary `jwt-tool`
- `katana` → binary `katana`
- `hakrawler` → binary `hakrawler`
- `gau` → binary `gau`
- `waybackurls` → binary `waybackurls`
- `zap-baseline` → binary `zap.sh`
- `jaeles` → binary `jaeles`
- `x8` → binary `x8`
- `uro` → binary `uro`
- `qsreplace` → binary `qsreplace`
- `anew` → binary `anew`
- `graphql-voyager` → binary `graphql-voyager`
- `evil-winrm` → binary `evil-winrm`
- `hashid` → binary `hashid`
- `ophcrack` → binary `ophcrack`
- `ghidra-headless` → binary `analyzeHeadless`
- `ropgadget` → binary `ROPgadget`
- `ropper` → binary `ropper`
- `one-gadget` → binary `one_gadget`
- `upx` → binary `upx`
- `volatility3` → binary `vol`
- `prowler` → binary `prowler`
- `scout-suite` → binary `scout`
- `kube-hunter` → binary `kube-hunter`
- `kube-bench` → binary `kube-bench`
- `docker-bench` → binary `docker-bench-security`
- `checkov` → binary `checkov`
- `terrascan` → binary `terrascan`
- `pacu` → binary `pacu`
- `cloudmapper` → binary `cloudmapper`
- ... and 42 more (see tool_inventory.json)

## Development Integration
- **Aegis Fusion:** Tool registry at `C:\AegisControlPlane\aegis\registry.py`
- **MCP Bridge:** `POST http://localhost:8899/` with `{"method":"tools/call","params":{"name":"nmap","target":"aegis-target"}}`
- **Re-run docs:** `python C:\GrokStrike\grokstrike_runner.py`
- **DVWA chains:** `full_assessment`, `injection`, `web_enum` in registry `DVWA_CHAINS`
