# john-ctf

## Tool Name & Category
- **Name:** john-ctf
- **Category:** ctf (CTF / Forensics — steganography, carving, memory analysis)
- **Binary:** `john`
- **Agent:** ctf
- **DVWA-optimized:** False

## Official Purpose
CTF password crack

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
john --format=raw-md5 /workspace/hash.txt
```

**Target:** `aegis-target`  
**Duration:** 0.08s | **Exit code:** 127

## Full Output Summary
```
bash: line 1: john: command not found

```

## What I Learned / Edge Cases / Gotchas
- Binary not installed in Kali container — apt install required
- Uses synthetic /workspace artifacts — not live target attack
- Registry template: `john --format=raw-md5 /workspace/hash.txt {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**1/10** — Limited output or tool not fully installed

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=aegis-target only; no destructive flags
- Timeout: 90s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:35.016846+00:00*
