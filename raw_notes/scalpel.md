# scalpel

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | ctf — CTF / Forensics |
| **Binary** | `scalpel` ✅ installed |
| **Agent** | forensics |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
Configurable file carving

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
scalpel -o /results/scalpel /workspace/disk.img
```

| Metric | Value |
|--------|-------|
| Duration | 0.1s |
| Exit code | 255 |
| Effectiveness | **3/10** — Minimal or error output |

## Key Findings
- No automated findings extracted — review output below

## Full Output Summary
```
Scalpel version 1.60
Written by Golden G. Richard III, based on Foremost 0.69.

--- STDERR ---

Opening target "/workspace/disk.img"

ERROR: The configuration file didn't specify any file types to carve.
(If you're using the default configuration file, you'll have to
uncomment some of the file types.)

See /etc/scalpel/scalpel.conf.

```

## What I Learned / Edge Cases / Gotchas
- Uses synthetic /workspace artifacts — swap in real samples for deeper RE/forensics
- Registry template: `scalpel -o /results/scalpel /workspace/disk.img {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 180s

## Next Steps for Exploration & Development
Run `scalpel --help` and tune `scalpel -o /results/scalpel /workspace/disk.img {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:48:31.492103+00:00*
