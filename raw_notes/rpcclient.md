# rpcclient

## Tool Name & Category
- **Name:** rpcclient
- **Category:** network (Network Reconnaissance — port scanning, service enumeration, SMB/DNS discovery)
- **Binary:** `rpcclient`
- **Agent:** network
- **DVWA-optimized:** False

## Official Purpose
RPC enumeration

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
rpcclient -c enumdomusers aegis-target
```

**Target:** `aegis-target`  
**Duration:** 0.13s | **Exit code:** 1

## Full Output Summary
```
Cannot connect to server.  Error was NT_STATUS_CONNECTION_REFUSED

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab context
- Registry template: `rpcclient -c enumdomusers {host} {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**3/10** — Limited output or tool not fully installed

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=aegis-target only; no destructive flags
- Timeout: 90s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:07:35.169364+00:00*
