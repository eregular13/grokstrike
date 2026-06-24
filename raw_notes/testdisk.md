# testdisk

## Tool Name & Category
- **Name:** testdisk
- **Category:** ctf (CTF / Forensics — steganography, carving, memory analysis)
- **Binary:** `testdisk`
- **Agent:** forensics
- **DVWA-optimized:** False

## Official Purpose
Partition recovery

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
testdisk /list /workspace/disk.img
```

**Target:** `aegis-target`  
**Duration:** 0.1s | **Exit code:** 127

## Full Output Summary
```
bash: line 1: testdisk: command not found

```

## What I Learned / Edge Cases / Gotchas
- Binary not installed in Kali container — apt install required
- Uses synthetic /workspace artifacts — not live target attack
- Registry template: `testdisk /list /workspace/disk.img {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**1/10** — Limited output or tool not fully installed

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=aegis-target only; no destructive flags
- Timeout: 90s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:33.812035+00:00*
