# host

## Tool Name & Category
- **Name:** host
- **Category:** network (Network Reconnaissance — port scanning, service enumeration, SMB/DNS discovery)
- **Binary:** `host`
- **Agent:** network
- **DVWA-optimized:** False

## Official Purpose
DNS host lookup

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
host -a aegis-target
```

**Target:** `aegis-target`  
**Duration:** 3.97s | **Exit code:** 1

## Full Output Summary
```
Trying "aegis-target"
Host aegis-target not found: 3(NXDOMAIN)
Received 30 bytes from 127.0.0.11#53 in 3836 ms
Received 30 bytes from 127.0.0.11#53 in 3836 ms

```

## What I Learned / Edge Cases / Gotchas
- Binary not installed in Kali container — apt install required
- Registry template: `host -a {host} {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**5/10** — Partial results; useful for learning workflow

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=aegis-target only; no destructive flags
- Timeout: 30s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:08:34.956473+00:00*
