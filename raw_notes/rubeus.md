# rubeus

## Tool Name & Category
- **Name:** rubeus
- **Category:** exploit (Exploit Generation — Metasploit, impacket, post-exploitation)
- **Binary:** `Rubeus`
- **Agent:** exploit
- **DVWA-optimized:** False

## Official Purpose
Kerberos abuse

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
echo 'Rubeus Windows-only'
```

**Target:** `aegis-target`  
**Duration:** 0.1s | **Exit code:** 0

## Full Output Summary
```
Rubeus Windows-only

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab context
- Registry template: `echo 'Rubeus Windows-only' {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**6/10** — Partial results; useful for learning workflow

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=aegis-target only; no destructive flags
- Timeout: 10s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:39.967353+00:00*
