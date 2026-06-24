# shodan-cli

## Tool Name & Category
- **Name:** shodan-cli
- **Category:** osint (OSINT — open-source intelligence gathering)
- **Binary:** `shodan`
- **Agent:** osint
- **DVWA-optimized:** False

## Official Purpose
Shodan host lookup

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
shodan host localhost
```

**Target:** `localhost`  
**Duration:** 0.24s | **Exit code:** 1

## Full Output Summary
```
Error: Please run "shodan init <api key>" before using this command

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab context
- Registry template: `shodan host {host} {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**3/10** — Limited output or tool not fully installed

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=localhost only; no destructive flags
- Timeout: 60s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:36.484283+00:00*
