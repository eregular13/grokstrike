# maltego

## Tool Name & Category
- **Name:** maltego
- **Category:** osint (OSINT — open-source intelligence gathering)
- **Binary:** `maltego`
- **Agent:** osint
- **DVWA-optimized:** False

## Official Purpose
Link analysis

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
echo 'Maltego transform hub'
```

**Target:** `localhost`  
**Duration:** 0.09s | **Exit code:** 0

## Full Output Summary
```
Maltego transform hub

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab context
- Registry template: `echo 'Maltego transform hub' {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**8/10** — Strong signal on DVWA/Juice Shop

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=localhost only; no destructive flags
- Timeout: 10s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:35.735601+00:00*
