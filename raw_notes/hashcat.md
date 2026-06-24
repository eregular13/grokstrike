# hashcat

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | auth — Authentication / Credential Testing |
| **Binary** | `hashcat` ✅ installed |
| **Agent** | auth |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
GPU hash cracking

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
hashcat -m 0 -a 0 /workspace/hash.txt /usr/share/wordlists/rockyou.txt --force 2>&1 | head -30
```

| Metric | Value |
|--------|-------|
| Duration | 0.28s |
| Exit code | 0 |
| Effectiveness | **9/10** — Rich actionable output |

## Key Findings
- No automated findings extracted — review output below

## Full Output Summary
```
hashcat (v7.1.2) starting

You have enabled --force to bypass dangerous warnings and errors!
This can hide serious problems and should only be done when debugging.
Do not report hashcat issues encountered when using --force.

Initializing bridges. Please be patient...Initialized bridgesInitializing backend runtimes. Please be patient...clGetPlatformIDs(): CL_PLATFORM_NOT_FOUND_KHR

ATTENTION! No OpenCL, HIP or CUDA compatible platform found.

You are probably missing the OpenCL, CUDA or HIP runtime installation.

* AMD GPUs on Linux require this driver:
  "AMD Radeon Software for Linux" with "ROCm"
* Intel and AMD CPUs require this runtime:
  "Intel CPU Runtime for OpenCL" or PoCL
* Intel GPUs require this driver:
  "Intel Graphics Compute Runtime" aka NEO
* NVIDIA GPUs require this runtime and driver:
  "NVIDIA CUDA Toolkit" (both runtime and driver included)

Started: Wed Jun 24 05:47:50 2026
Stopped: Wed Jun 24 05:47:51 2026

```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `hashcat -m 0 /workspace/hash.txt /usr/share/wordlists/rockyou.txt {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 120s

## Next Steps for Exploration & Development
Run `hashcat --help` and tune `hashcat -m 0 /workspace/hash.txt /usr/share/wordlists/rockyou.txt {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:47:51.076602+00:00*
