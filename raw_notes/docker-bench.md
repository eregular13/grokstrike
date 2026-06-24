# docker-bench

## Tool Name & Category
- **Name:** docker-bench
- **Category:** cloud (Cloud & Container Security — K8s, AWS, container image scanning)
- **Binary:** `docker-bench-security`
- **Agent:** cloud
- **DVWA-optimized:** False

## Official Purpose
Docker CIS benchmark

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
docker-bench-security
```

**Target:** `aegis-target`  
**Duration:** 0.1s | **Exit code:** 127

## Full Output Summary
```
bash: line 1: docker-bench-security: command not found

```

## What I Learned / Edge Cases / Gotchas
- Binary not installed in Kali container — apt install required
- Cloud tools need credentials/config — version/help checks only in lab
- Registry template: `docker-bench-security {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**1/10** — Limited output or tool not fully installed

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=aegis-target only; no destructive flags
- Timeout: 90s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:32.145672+00:00*
