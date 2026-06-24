# angr-check

## Tool Name & Category
- **Name:** angr-check
- **Category:** binary (Binary Analysis / Reverse Engineering — disassembly, debugging, firmware)
- **Binary:** `python3`
- **Agent:** binary
- **DVWA-optimized:** False

## Official Purpose
Angr symbolic execution

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
python3 -c "import angr; print('angr ready')"
```

**Target:** `aegis-target`  
**Duration:** 0.12s | **Exit code:** 1

## Full Output Summary
```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import angr; print('angr ready')
    ^^^^^^^^^^^
ModuleNotFoundError: No module named 'angr'

```

## What I Learned / Edge Cases / Gotchas
- Uses synthetic /workspace artifacts — not live target attack
- Registry template: `python3 -c "import angr; print('angr ready')" {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**3/10** — Limited output or tool not fully installed

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=aegis-target only; no destructive flags
- Timeout: 30s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:30.339214+00:00*
