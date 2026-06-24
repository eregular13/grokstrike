# nbtscan

## Tool Name & Category
- **Name:** nbtscan
- **Category:** network (Network Reconnaissance — port scanning, service enumeration, SMB/DNS discovery)
- **Binary:** `nbtscan`
- **Agent:** network
- **DVWA-optimized:** False

## Official Purpose
NetBIOS scan

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
nbtscan aegis-target
```

**Target:** `aegis-target`  
**Duration:** 0.08s | **Exit code:** 127

## Full Output Summary
```
bash: line 1: nbtscan: command not found

```

## What I Learned / Edge Cases / Gotchas
- Binary not installed in Kali container — apt install required
- Registry template: `nbtscan {host} {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**1/10** — Limited output or tool not fully installed

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=aegis-target only; no destructive flags
- Timeout: 60s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:07:35.036888+00:00*
