# maigret

## Tool Name & Category
- **Name:** maigret
- **Category:** osint (OSINT — open-source intelligence gathering)
- **Binary:** `maigret`
- **Agent:** osint
- **DVWA-optimized:** False

## Official Purpose
Username OSINT

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
maigret username
```

**Target:** `localhost`  
**Duration:** 0.09s | **Exit code:** 127

## Full Output Summary
```
bash: line 1: maigret: command not found

```

## What I Learned / Edge Cases / Gotchas
- Binary not installed in Kali container — apt install required
- Registry template: `maigret username {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**1/10** — Limited output or tool not fully installed

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=localhost only; no destructive flags
- Timeout: 90s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:37.495209+00:00*
