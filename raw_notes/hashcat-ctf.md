# hashcat-ctf

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | ctf — CTF / Forensics |
| **Binary** | `hashcat` ✅ installed |
| **Agent** | ctf |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
CTF hash crack

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
hashcat -m 1000 /workspace/ntlm.hash /usr/share/wordlists/rockyou.txt
```

| Metric | Value |
|--------|-------|
| Duration | 0.27s |
| Exit code | 255 |
| Effectiveness | **5/10** — Non-zero exit but useful output |

## Key Findings
- No automated findings extracted — review output below

## Full Output Summary
```
hashcat (v7.1.2) starting

Initializing bridges. Please be patient...Initialized bridgesInitializing backend runtimes. Please be patient...You are probably missing the OpenCL, CUDA or HIP runtime installation.

* AMD GPUs on Linux require this driver:
  "AMD Radeon Software for Linux" with "ROCm"
* Intel and AMD CPUs require this runtime:
  "Intel CPU Runtime for OpenCL" or PoCL
* Intel GPUs require this driver:
  "Intel Graphics Compute Runtime" aka NEO
* NVIDIA GPUs require this runtime and driver:
  "NVIDIA CUDA Toolkit" (both runtime and driver included)

Started: Wed Jun 24 05:48:32 2026
Stopped: Wed Jun 24 05:48:33 2026

--- STDERR ---
clGetPlatformIDs(): CL_PLATFORM_NOT_FOUND_KHR

ATTENTION! No OpenCL, HIP or CUDA compatible platform found.


```

## What I Learned / Edge Cases / Gotchas
- Uses synthetic /workspace artifacts — swap in real samples for deeper RE/forensics
- Registry template: `hashcat -m 1000 /workspace/ntlm.hash /usr/share/wordlists/rockyou.txt {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 180s

## Next Steps for Exploration & Development
Run `hashcat --help` and tune `hashcat -m 1000 /workspace/ntlm.hash /usr/share/wordlists/rockyou.txt {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:48:33.132438+00:00*
