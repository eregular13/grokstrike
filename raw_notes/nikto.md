# nikto

## Tool Name & Category
- **Name:** nikto
- **Category:** web (Web Application Security — crawling, fuzzing, vulnerability scanning)
- **Binary:** `nikto`
- **Agent:** web
- **DVWA-optimized:** True

## Official Purpose
Web server vulnerability scan

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
nikto -h http://aegis-target
```

**Target:** `http://aegis-target`  
**Duration:** 120.02s | **Exit code:** -1

## Full Output Summary
```
TIMEOUT after 120s
```

## What I Learned / Edge Cases / Gotchas
- Command exceeded safe timeout — increase for full scans
- Registry template: `nikto -h {web} {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**3/10** — Limited output or tool not fully installed

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=http://aegis-target only; no destructive flags
- Timeout: 90s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:10:54.655659+00:00*
