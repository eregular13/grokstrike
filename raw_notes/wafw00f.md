# wafw00f

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | web — Web Application Security |
| **Binary** | `wafw00f` ✅ installed |
| **Agent** | web |
| **DVWA-optimized** | True |
| **Lab target** | `http://aegis-target` |

## Official Purpose
WAF fingerprinting

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
wafw00f -a http://aegis-target 2>&1
```

| Metric | Value |
|--------|-------|
| Duration | 0.23s |
| Exit code | 0 |
| Effectiveness | **9/10** — Rich actionable output |

## Key Findings
- No automated findings extracted — review output below

## Full Output Summary
```

                   [1;97m______
                  [1;97m/      \
                 [1;97m(  Woof! )
                  [1;97m\  ____/                      [1;91m)
                  [1;97m,,                           [1;91m) ([1;93m_
             [1;93m.-. [1;97m-    [1;92m_______                 [1;91m( [1;93m|__|
            [1;93m()``; [1;92m|==|_______)                [1;91m.)[1;93m|__|
            [1;93m/ ('        [1;92m/|\                  [1;91m(  [1;93m|__|
        [1;93m(  /  )       [1;92m / | \                  [1;91m. [1;93m|__|
         [1;93m\(_)_))      [1;92m/  |  \                   [1;93m|__|[0m

                    [1;96m~ WAFW00F : [1;94mv2.4.2 ~[1;97m
    The Web Application Firewall Fingerprinting Toolkit
    [0m
[*] Checking http://aegis-target
[+] Generic Detection results:
[-] No WAF detected by the generic detection
[~] Number of requests: 7

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `wafw00f {web} {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 60s

## Next Steps for Exploration & Development
Run `wafw00f --help` and tune `wafw00f {web} {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:47:41.101642+00:00*
