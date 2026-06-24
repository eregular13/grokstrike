# jaeles

## Tool Name & Category
- **Name:** jaeles
- **Category:** web (Web Application Security — crawling, fuzzing, vulnerability scanning)
- **Binary:** `jaeles`
- **Agent:** web
- **DVWA-optimized:** True

## Official Purpose
Signature vuln scanner

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
jaeles scan -u http://aegis-target
```

**Target:** `http://aegis-target`  
**Duration:** 0.1s | **Exit code:** 127

## Full Output Summary
```
bash: line 1: jaeles: command not found

```

## What I Learned / Edge Cases / Gotchas
- Binary not installed in Kali container — apt install required
- Registry template: `jaeles scan -u {web} {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**1/10** — Limited output or tool not fully installed

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=http://aegis-target only; no destructive flags
- Timeout: 90s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:26.848540+00:00*
