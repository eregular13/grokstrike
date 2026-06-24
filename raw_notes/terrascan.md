# terrascan

## Tool Name & Category
- **Name:** terrascan
- **Category:** cloud (Cloud & Container Security — K8s, AWS, container image scanning)
- **Binary:** `terrascan`
- **Agent:** cloud
- **DVWA-optimized:** False

## Official Purpose
IaC policy scan

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
terrascan scan -d /workspace/iac
```

**Target:** `aegis-target`  
**Duration:** 0.11s | **Exit code:** 127

## Full Output Summary
```
bash: line 1: terrascan: command not found

```

## What I Learned / Edge Cases / Gotchas
- Binary not installed in Kali container — apt install required
- Cloud tools need credentials/config — version/help checks only in lab
- Registry template: `terrascan scan -d /workspace/iac {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**1/10** — Limited output or tool not fully installed

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=aegis-target only; no destructive flags
- Timeout: 90s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:32.366320+00:00*
