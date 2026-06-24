# h8mail

## Tool Name & Category
- **Name:** h8mail
- **Category:** osint (OSINT — open-source intelligence gathering)
- **Binary:** `h8mail`
- **Agent:** osint
- **DVWA-optimized:** False

## Official Purpose
Email breach search

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
h8mail -t test@localhost
```

**Target:** `localhost`  
**Duration:** 0.1s | **Exit code:** 127

## Full Output Summary
```
bash: line 1: h8mail: command not found

```

## What I Learned / Edge Cases / Gotchas
- Binary not installed in Kali container — apt install required
- Registry template: `h8mail -t test@{host} {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**1/10** — Limited output or tool not fully installed

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=localhost only; no destructive flags
- Timeout: 90s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:36.132090+00:00*
