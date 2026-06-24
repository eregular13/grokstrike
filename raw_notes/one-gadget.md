# one-gadget

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | binary — Binary Analysis / Reverse Engineering |
| **Binary** | `one_gadget` ❌ missing |
| **Agent** | binary |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
One-shot RCE gadgets

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
one_gadget /lib/x86_64-linux-gnu/libc.so.6
```

| Metric | Value |
|--------|-------|
| Duration | 0.0s |
| Exit code | 127 |
| Effectiveness | **1/10** — Tool binary not installed |

## Key Findings
- No automated findings extracted — review output below

## Full Output Summary
```

--- STDERR ---
command not found: one_gadget
```

## What I Learned / Edge Cases / Gotchas
- `one_gadget` not found — run `scripts/kali-full-bootstrap.sh`
- Uses synthetic /workspace artifacts — swap in real samples for deeper RE/forensics
- Registry template: `one_gadget /lib/x86_64-linux-gnu/libc.so.6 {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 60s

## Next Steps for Exploration & Development
Run `one_gadget --help` and tune `one_gadget /lib/x86_64-linux-gnu/libc.so.6 {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:47:56.369246+00:00*
