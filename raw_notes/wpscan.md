# wpscan

## Tool Name & Category
- **Name:** wpscan
- **Category:** web (Web Application Security — crawling, fuzzing, vulnerability scanning)
- **Binary:** `wpscan`
- **Agent:** web
- **DVWA-optimized:** False

## Official Purpose
WordPress scanner

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
wpscan --url http://aegis-juice:3000 --enumerate vp,vt
```

**Target:** `http://aegis-juice:3000`  
**Duration:** 0.09s | **Exit code:** 127

## Full Output Summary
```
bash: line 1: wpscan: command not found

```

## What I Learned / Edge Cases / Gotchas
- Binary not installed in Kali container — apt install required
- Registry template: `wpscan --url {web} --enumerate vp,vt {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**1/10** — Limited output or tool not fully installed

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=http://aegis-juice:3000 only; no destructive flags
- Timeout: 90s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:24.711754+00:00*
