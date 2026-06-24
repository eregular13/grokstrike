# wafw00f

## Tool Name & Category
- **Name:** wafw00f
- **Category:** web (Web Application Security — crawling, fuzzing, vulnerability scanning)
- **Binary:** `wafw00f`
- **Agent:** web
- **DVWA-optimized:** True

## Official Purpose
WAF fingerprinting

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
wafw00f http://aegis-target
```

**Target:** `http://aegis-target`  
**Duration:** 0.21s | **Exit code:** 0

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
- Executed successfully in isolated lab context
- Registry template: `wafw00f {web} {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**8/10** — Strong signal on DVWA/Juice Shop

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=http://aegis-target only; no destructive flags
- Timeout: 60s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:25.217289+00:00*
