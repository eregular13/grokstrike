# crackmapexec

## Tool Name & Category
- **Name:** crackmapexec
- **Category:** network (Network Reconnaissance — port scanning, service enumeration, SMB/DNS discovery)
- **Binary:** `crackmapexec`
- **Agent:** network
- **DVWA-optimized:** False

## Official Purpose
Network pentest Swiss army knife

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
crackmapexec smb aegis-target
```

**Target:** `aegis-target`  
**Duration:** 0.61s | **Exit code:** 0

## Full Output Summary
```

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab context
- Registry template: `crackmapexec smb {host} {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**6/10** — Partial results; useful for learning workflow

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=aegis-target only; no destructive flags
- Timeout: 90s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:08:26.430197+00:00*
