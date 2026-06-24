# httpx

## Tool Name & Category
- **Name:** httpx
- **Category:** web (Web Application Security — crawling, fuzzing, vulnerability scanning)
- **Binary:** `httpx`
- **Agent:** web
- **DVWA-optimized:** True

## Official Purpose
HTTP probe + tech detect

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
httpx -u http://aegis-target -title -tech-detect -status-code
```

**Target:** `http://aegis-target`  
**Duration:** 0.18s | **Exit code:** 2

## Full Output Summary
```
Usage: httpx [OPTIONS] URL

Error: No such option: -u

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab context
- Registry template: `httpx -u {web} -title -tech-detect -status-code {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**3/10** — Limited output or tool not fully installed

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=http://aegis-target only; no destructive flags
- Timeout: 60s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:08:35.229955+00:00*
