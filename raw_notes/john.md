# john

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | auth — Authentication / Credential Testing |
| **Binary** | `john` ✅ installed |
| **Agent** | auth |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
Password hash cracking

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt /workspace/hash.txt 2>&1 | head -30
```

| Metric | Value |
|--------|-------|
| Duration | 0.26s |
| Exit code | 0 |
| Effectiveness | **9/10** — Rich actionable output |

## Key Findings
- No automated findings extracted — review output below

## Full Output Summary
```
Created directory: /root/.john
Using default input encoding: UTF-8
Loaded 2 password hashes with no different salts (Raw-MD5 [MD5 512/512 AVX512BW 16x3])
Warning: no OpenMP support for this hash type, consider --fork=16
Press Ctrl-C to abort, or send SIGUSR1 to john process for status
hello            (?)     
test             (?)     
2g 0:00:00:00 DONE (2026-06-24 05:47) 100.0g/s 8332Kp/s 8332Kc/s 8371KC/s tyson4..solveig
Use the "--show --format=Raw-MD5" options to display all of the cracked passwords reliably
Session completed. 

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `john --wordlist=/usr/share/wordlists/rockyou.txt /workspace/hash.txt {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 120s

## Next Steps for Exploration & Development
Run `john --help` and tune `john --wordlist=/usr/share/wordlists/rockyou.txt /workspace/hash.txt {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:47:50.686040+00:00*
