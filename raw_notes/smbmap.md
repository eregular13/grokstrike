# smbmap

## Tool Name & Category
- **Name:** smbmap
- **Category:** network (Network Reconnaissance — port scanning, service enumeration, SMB/DNS discovery)
- **Binary:** `smbmap`
- **Agent:** network
- **DVWA-optimized:** False

## Official Purpose
SMB share mapping

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
smbmap -H aegis-target
```

**Target:** `aegis-target`  
**Duration:** 0.1s | **Exit code:** 127

## Full Output Summary
```
bash: line 1: smbmap: command not found

```

## What I Learned / Edge Cases / Gotchas
- Binary not installed in Kali container — apt install required
- Registry template: `smbmap -H {host} {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**1/10** — Limited output or tool not fully installed

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=aegis-target only; no destructive flags
- Timeout: 90s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:07:55.625428+00:00*
