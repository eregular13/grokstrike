# sleuthkit-fls

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | ctf — CTF / Forensics |
| **Binary** | `fls` ✅ installed |
| **Agent** | forensics |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
File listing from image

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
fls -r /workspace/disk.img
```

| Metric | Value |
|--------|-------|
| Duration | 0.12s |
| Exit code | 1 |
| Effectiveness | **3/10** — Minimal or error output |

## Key Findings
- No automated findings extracted — review output below

## Full Output Summary
```

--- STDERR ---
Cannot determine file system type

```

## What I Learned / Edge Cases / Gotchas
- Uses synthetic /workspace artifacts — swap in real samples for deeper RE/forensics
- Registry template: `fls -r /workspace/disk.img {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 120s

## Next Steps for Exploration & Development
Run `fls --help` and tune `fls -r /workspace/disk.img {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:48:31.908788+00:00*
