# jwt-tool

## Tool Name & Category
- **Name:** jwt-tool
- **Category:** web (Web Application Security — crawling, fuzzing, vulnerability scanning)
- **Binary:** `jwt-tool`
- **Agent:** web
- **DVWA-optimized:** False

## Official Purpose
JWT testing

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
jwt-tool -t http://aegis-juice:3000
```

**Target:** `http://aegis-juice:3000`  
**Duration:** 0.09s | **Exit code:** 127

## Full Output Summary
```
bash: line 1: jwt-tool: command not found

```

## What I Learned / Edge Cases / Gotchas
- Binary not installed in Kali container — apt install required
- Registry template: `jwt-tool -t {web} {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**1/10** — Limited output or tool not fully installed

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=http://aegis-juice:3000 only; no destructive flags
- Timeout: 90s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:25.928510+00:00*
