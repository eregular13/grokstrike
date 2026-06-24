# nosqlmap

## Tool Name & Category
- **Name:** nosqlmap
- **Category:** web (Web Application Security — crawling, fuzzing, vulnerability scanning)
- **Binary:** `nosqlmap`
- **Agent:** web
- **DVWA-optimized:** False

## Official Purpose
NoSQL injection

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
nosqlmap -u http://aegis-juice:3000
```

**Target:** `http://aegis-juice:3000`  
**Duration:** 0.1s | **Exit code:** 127

## Full Output Summary
```
bash: line 1: nosqlmap: command not found

```

## What I Learned / Edge Cases / Gotchas
- Binary not installed in Kali container — apt install required
- Registry template: `nosqlmap -u {web} {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**1/10** — Limited output or tool not fully installed

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=http://aegis-juice:3000 only; no destructive flags
- Timeout: 90s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:25.731601+00:00*
