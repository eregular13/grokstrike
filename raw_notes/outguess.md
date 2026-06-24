# outguess

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | ctf — CTF / Forensics |
| **Binary** | `outguess` ❌ missing |
| **Agent** | forensics |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
JPEG steganography

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
outguess -r /workspace/image.jpg /workspace/out
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
command not found: outguess
```

## What I Learned / Edge Cases / Gotchas
- `outguess` not found — run `scripts/kali-full-bootstrap.sh`
- Uses synthetic /workspace artifacts — swap in real samples for deeper RE/forensics
- Registry template: `outguess -r /workspace/image.jpg /workspace/out {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 60s

## Next Steps for Exploration & Development
Run `outguess --help` and tune `outguess -r /workspace/image.jpg /workspace/out {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:48:31.283577+00:00*
