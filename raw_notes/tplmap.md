# tplmap

## Tool Name & Category
- **Name:** tplmap
- **Category:** web (Web Application Security — crawling, fuzzing, vulnerability scanning)
- **Binary:** `tplmap`
- **Agent:** web
- **DVWA-optimized:** True

## Official Purpose
SSTI exploitation

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
tplmap -u http://aegis-target
```

**Target:** `http://aegis-target`  
**Duration:** 0.1s | **Exit code:** 127

## Full Output Summary
```
bash: line 1: tplmap: command not found

```

## What I Learned / Edge Cases / Gotchas
- Binary not installed in Kali container — apt install required
- Registry template: `tplmap -u {web} {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**1/10** — Limited output or tool not fully installed

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=http://aegis-target only; no destructive flags
- Timeout: 90s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:25.833062+00:00*
