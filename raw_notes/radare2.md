# radare2

## Tool Name & Category
- **Name:** radare2
- **Category:** binary (Binary Analysis / Reverse Engineering — disassembly, debugging, firmware)
- **Binary:** `r2`
- **Agent:** binary
- **DVWA-optimized:** False

## Official Purpose
Reverse engineering

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
r2 -A /workspace/binary -q -c 'afl'
```

**Target:** `aegis-target`  
**Duration:** 0.08s | **Exit code:** 127

## Full Output Summary
```
bash: line 1: r2: command not found

```

## What I Learned / Edge Cases / Gotchas
- Binary not installed in Kali container — apt install required
- Uses synthetic /workspace artifacts — not live target attack
- Registry template: `r2 -A /workspace/binary -q -c 'afl' {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**1/10** — Limited output or tool not fully installed

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=aegis-target only; no destructive flags
- Timeout: 90s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:29.218685+00:00*
