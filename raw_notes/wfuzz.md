# wfuzz

## Tool Name & Category
- **Name:** wfuzz
- **Category:** web (Web Application Security — crawling, fuzzing, vulnerability scanning)
- **Binary:** `wfuzz`
- **Agent:** web
- **DVWA-optimized:** True

## Official Purpose
Web fuzzer

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
wfuzz -c -z file,/usr/share/wordlists/dirb/common.txt --hc 404 http://aegis-target/FUZZ
```

**Target:** `http://aegis-target`  
**Duration:** 0.62s | **Exit code:** 0

## Full Output Summary
```
default
default
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
 /usr/lib/python3/dist-packages/wfuzz/wfuzz.py:78: UserWarning:Fatal exception: Error opening file. [Errno 2] No such file or directory: '/usr/share/wordlists/dirb/common.txt'

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab context
- Registry template: `wfuzz -c -z file,/usr/share/wordlists/dirb/common.txt --hc 404 {web}/FUZZ {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**6/10** — Partial results; useful for learning workflow

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=http://aegis-target only; no destructive flags
- Timeout: 90s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:22.669592+00:00*
