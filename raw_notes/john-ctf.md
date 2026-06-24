# john-ctf

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | ctf — CTF / Forensics |
| **Binary** | `john` ✅ installed |
| **Agent** | ctf |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
CTF password crack

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
john --format=raw-md5 /workspace/hash.txt
```

| Metric | Value |
|--------|-------|
| Duration | 0.22s |
| Exit code | 0 |
| Effectiveness | **9/10** — Rich actionable output |

## Key Findings
- No automated findings extracted — review output below

## Full Output Summary
```
Loaded 2 password hashes with no different salts (Raw-MD5 [MD5 512/512 AVX512BW 16x3])
No password hashes left to crack (see FAQ)

--- STDERR ---
Using default input encoding: UTF-8

```

## What I Learned / Edge Cases / Gotchas
- Uses synthetic /workspace artifacts — swap in real samples for deeper RE/forensics
- Registry template: `john --format=raw-md5 /workspace/hash.txt {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 180s

## Next Steps for Exploration & Development
Run `john --help` and tune `john --format=raw-md5 /workspace/hash.txt {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:48:33.454854+00:00*
