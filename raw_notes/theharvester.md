# theharvester

## Tool Name & Category
- **Name:** theharvester
- **Category:** network (Network Reconnaissance — port scanning, service enumeration, SMB/DNS discovery)
- **Binary:** `theharvester`
- **Agent:** osint
- **DVWA-optimized:** False

## Official Purpose
Email/subdomain harvest

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
theHarvester -d aegis-target -b all
```

**Target:** `aegis-target`  
**Duration:** 90.02s | **Exit code:** -1

## Full Output Summary
```
TIMEOUT after 90s
```

## What I Learned / Edge Cases / Gotchas
- Command exceeded safe timeout — increase for full scans
- Registry template: `theHarvester -d {host} -b all {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**3/10** — Limited output or tool not fully installed

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=aegis-target only; no destructive flags
- Timeout: 90s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:07:34.857957+00:00*
