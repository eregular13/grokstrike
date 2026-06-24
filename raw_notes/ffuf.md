# ffuf

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | web — Web Application Security |
| **Binary** | `ffuf` ✅ installed |
| **Agent** | web |
| **DVWA-optimized** | True |
| **Lab target** | `http://aegis-target` |

## Official Purpose
Fast web fuzzer

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
ffuf -u http://aegis-target/FUZZ -w /usr/share/wordlists/dirb/common.txt -mc 200,301,302,403 -t 20
```

| Metric | Value |
|--------|-------|
| Duration | 0.37s |
| Exit code | 0 |
| Effectiveness | **9/10** — Rich actionable output |

## Key Findings
- **HTTP discovery:** Status: 403
- **HTTP discovery:** Status: 302
- **HTTP discovery:** Status: 403
- **HTTP discovery:** Status: 403
- **HTTP discovery:** Status: 301
- **HTTP discovery:** Status: 301
- **HTTP discovery:** Status: 301
- **HTTP discovery:** Status: 200

## Full Output Summary
```

[2K.htpasswd               [Status: 403, Size: 296, Words: 22, Lines: 12, Duration: 0ms][0m

[2K                        [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 1ms][0m

[2K.hta                    [Status: 403, Size: 291, Words: 22, Lines: 12, Duration: 0ms][0m

[2K.htaccess               [Status: 403, Size: 296, Words: 22, Lines: 12, Duration: 0ms][0m

[2Kconfig                  [Status: 301, Size: 313, Words: 20, Lines: 10, Duration: 0ms][0m

[2Kdocs                    [Status: 301, Size: 311, Words: 20, Lines: 10, Duration: 0ms][0m

[2Kexternal                [Status: 301, Size: 315, Words: 20, Lines: 10, Duration: 0ms][0m

[2Kfavicon.ico             [Status: 200, Size: 1406, Words: 5, Lines: 2, Duration: 0ms][0m

[2Kindex.php               [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 1ms][0m

[2Kphp.ini                 [Status: 200, Size: 148, Words: 17, Lines: 5, Duration: 0ms][0m

[2Kphpinfo.php             [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 0ms][0m

[2Krobots.txt              [Status: 200, Size: 26, Words: 3, Lines: 2, Duration: 0ms][0m

[2Kserver-status           [Status: 403, Size: 300, Words: 22, Lines: 12, Duration: 0ms][0m

--- STDERR ---

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://aegis-target/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirb/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 20
 :: Matcher          : Response status: 200,301,302,403
________________________________________________


[2K:: Progress: [1/4614] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0 ::
[2K:: Progress: [20/4614] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0 ::
[2K:: Progress: [23/4614] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0 ::
[2K:: Progress: [25/4614] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0 ::
[2K:: Progress: [34/4614] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0 ::
[2K:: Progress: [1035/4614] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0 ::
[2K:: Progress: [1335/4614] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0 ::
[2K:: Progress: [1562/4614] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0 ::
[2K:: Progress: [1603/4614] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0 ::
[2K:: Progress: [2048/4614] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0 ::
[2K:: Progress: [2610/4614] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0 ::
[2K:: Progress: [2938/4614] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0 ::
[2K:: Progress: [2979/4614] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0 ::
[2K:: Progress: [3451/4614] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0 ::
[2K:: Progress: [3603/4614] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0 ::
[2K:: Progress: [4614/4614] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0 ::
[2K:: Progress: [4614/4614] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0 ::

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `ffuf -u {web}/FUZZ -w /usr/share/wordlists/dirb/common.txt -mc 200,301,302 {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 120s

## Next Steps for Exploration & Development
Run `ffuf --help` and tune `ffuf -u {web}/FUZZ -w /usr/share/wordlists/dirb/common.txt -mc 200,301,302 {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:47:33.577254+00:00*
