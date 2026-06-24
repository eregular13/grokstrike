# dalfox

## Tool Name & Category
- **Name:** dalfox
- **Category:** web (Web Application Security — crawling, fuzzing, vulnerability scanning)
- **Binary:** `dalfox`
- **Agent:** web
- **DVWA-optimized:** True

## Official Purpose
XSS scanner

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
dalfox url http://aegis-target
```

**Target:** `http://aegis-target`  
**Duration:** 0.11s | **Exit code:** 127

## Full Output Summary
```
bash: line 1: dalfox: command not found

```

## What I Learned / Edge Cases / Gotchas
- Binary not installed in Kali container — apt install required
- Registry template: `dalfox url {web} {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**1/10** — Limited output or tool not fully installed

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=http://aegis-target only; no destructive flags
- Timeout: 90s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:25.008385+00:00*
