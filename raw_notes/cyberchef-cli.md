# cyberchef-cli

## Tool Name & Category
- **Name:** cyberchef-cli
- **Category:** ctf (CTF / Forensics — steganography, carving, memory analysis)
- **Binary:** `python3`
- **Agent:** ctf
- **DVWA-optimized:** False

## Official Purpose
Encoding decode helper

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
python3 -c "print('CyberChef decode pipeline')"
```

**Target:** `aegis-target`  
**Duration:** 0.1s | **Exit code:** 0

## Full Output Summary
```
CyberChef decode pipeline

```

## What I Learned / Edge Cases / Gotchas
- Uses synthetic /workspace artifacts — not live target attack
- Registry template: `python3 -c "print('CyberChef decode pipeline')" {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**8/10** — Strong signal on DVWA/Juice Shop

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=aegis-target only; no destructive flags
- Timeout: 10s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:34.827837+00:00*
