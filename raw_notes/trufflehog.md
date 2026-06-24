# trufflehog

## Tool Name & Category
- **Name:** trufflehog
- **Category:** osint (OSINT — open-source intelligence gathering)
- **Binary:** `trufflehog`
- **Agent:** osint
- **DVWA-optimized:** False

## Official Purpose
Secret scanning

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
trufflehog filesystem /workspace
```

**Target:** `localhost`  
**Duration:** 0.1s | **Exit code:** 127

## Full Output Summary
```
bash: line 1: trufflehog: command not found

```

## What I Learned / Edge Cases / Gotchas
- Binary not installed in Kali container — apt install required
- Registry template: `trufflehog filesystem /workspace {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**1/10** — Limited output or tool not fully installed

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=localhost only; no destructive flags
- Timeout: 90s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:37.691655+00:00*
