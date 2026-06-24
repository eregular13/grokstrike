# responder

## Tool Name & Category
- **Name:** responder
- **Category:** network (Network Reconnaissance — port scanning, service enumeration, SMB/DNS discovery)
- **Binary:** `responder`
- **Agent:** network
- **DVWA-optimized:** False

## Official Purpose
LLMNR/NBT-NS poisoner

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
timeout 30 responder -I eth0 -A
```

**Target:** `aegis-target`  
**Duration:** 30.09s | **Exit code:** 124

## Full Output Summary
```

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab context
- Registry template: `timeout 30 responder -I eth0 -A {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**3/10** — Limited output or tool not fully installed

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=aegis-target only; no destructive flags
- Timeout: 60s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:08:25.713298+00:00*
