# nc

## Tool Name & Category
- **Name:** nc
- **Category:** network (Network Reconnaissance — port scanning, service enumeration, SMB/DNS discovery)
- **Binary:** `nc`
- **Agent:** network
- **DVWA-optimized:** True

## Official Purpose
Port connectivity check

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
nc -zv aegis-target 80 443 8080
```

**Target:** `aegis-target`  
**Duration:** 0.09s | **Exit code:** 0

## Full Output Summary
```
DNS fwd/rev mismatch: aegis-target != aegis-target.aegiscontrolplane_default
aegis-target [172.22.0.2] 80 (http) open

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab context
- Registry template: `nc -zv {host} 80 443 8080 {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**6/10** — Partial results; useful for learning workflow

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=aegis-target only; no destructive flags
- Timeout: 30s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:08:35.045636+00:00*
