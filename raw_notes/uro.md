# uro

## Tool Name & Category
- **Name:** uro
- **Category:** web (Web Application Security — crawling, fuzzing, vulnerability scanning)
- **Binary:** `uro`
- **Agent:** web
- **DVWA-optimized:** False

## Official Purpose
URL deduplication

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
cat /dev/stdin | uro
```

**Target:** `http://aegis-juice:3000`  
**Duration:** 0.1s | **Exit code:** 127

## Full Output Summary
```
bash: line 1: uro: command not found

```

## What I Learned / Edge Cases / Gotchas
- Binary not installed in Kali container — apt install required
- Registry template: `cat /dev/stdin | uro {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**1/10** — Limited output or tool not fully installed

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=http://aegis-juice:3000 only; no destructive flags
- Timeout: 30s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:27.044989+00:00*
