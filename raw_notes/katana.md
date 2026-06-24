# katana

## Tool Name & Category
- **Name:** katana
- **Category:** web (Web Application Security — crawling, fuzzing, vulnerability scanning)
- **Binary:** `katana`
- **Agent:** web
- **DVWA-optimized:** True

## Official Purpose
Next-gen crawler

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
katana -u http://aegis-target -silent
```

**Target:** `http://aegis-target`  
**Duration:** 0.11s | **Exit code:** 127

## Full Output Summary
```
bash: line 1: katana: command not found

```

## What I Learned / Edge Cases / Gotchas
- Binary not installed in Kali container — apt install required
- Registry template: `katana -u {web} -silent {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**1/10** — Limited output or tool not fully installed

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=http://aegis-target only; no destructive flags
- Timeout: 90s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:26.036136+00:00*
