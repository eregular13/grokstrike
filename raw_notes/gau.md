# gau

## Tool Name & Category
- **Name:** gau
- **Category:** web (Web Application Security — crawling, fuzzing, vulnerability scanning)
- **Binary:** `gau`
- **Agent:** osint
- **DVWA-optimized:** False

## Official Purpose
URL gathering

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
gau aegis-juice
```

**Target:** `http://aegis-juice:3000`  
**Duration:** 0.1s | **Exit code:** 127

## Full Output Summary
```
bash: line 1: gau: command not found

```

## What I Learned / Edge Cases / Gotchas
- Binary not installed in Kali container — apt install required
- Registry template: `gau {host} {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**1/10** — Limited output or tool not fully installed

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=http://aegis-juice:3000 only; no destructive flags
- Timeout: 90s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:26.231995+00:00*
