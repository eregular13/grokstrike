# recon-ng

## Tool Name & Category
- **Name:** recon-ng
- **Category:** osint (OSINT — open-source intelligence gathering)
- **Binary:** `recon-ng`
- **Agent:** osint
- **DVWA-optimized:** False

## Official Purpose
Recon-ng framework

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
recon-ng -w /workspace -C 'marketplace install all'
```

**Target:** `localhost`  
**Duration:** 0.11s | **Exit code:** 127

## Full Output Summary
```
bash: line 1: recon-ng: command not found

```

## What I Learned / Edge Cases / Gotchas
- Binary not installed in Kali container — apt install required
- Registry template: `recon-ng -w /workspace -C 'marketplace install all' {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**1/10** — Limited output or tool not fully installed

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=localhost only; no destructive flags
- Timeout: 90s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:35.640154+00:00*
