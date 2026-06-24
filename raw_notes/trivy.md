# trivy

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | cloud — Cloud & Container Security |
| **Binary** | `trivy` ✅ installed |
| **Agent** | cloud |
| **DVWA-optimized** | False |
| **Lab target** | `aegis-target` |

## Official Purpose
Container vuln scan

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
trivy image --scanners vuln --severity HIGH,CRITICAL kalilinux/kali-rolling 2>&1 | head -50
```

| Metric | Value |
|--------|-------|
| Duration | 25.89s |
| Exit code | 0 |
| Effectiveness | **9/10** — Rich actionable output |

## Key Findings
- See output summary for raw tool data.

## Full Output Summary
```
2026-06-24T05:48:02Z	INFO	[vulndb] Need to update DB
2026-06-24T05:48:02Z	INFO	[vulndb] Downloading vulnerability DB...
2026-06-24T05:48:02Z	INFO	[vulndb] Downloading artifact...	repo="mirror.gcr.io/aquasec/trivy-db:2"
842.92 KiB / 97.04 MiB [>____________________________________________________________] 0.85% ? p/s ?2.76 MiB / 97.04 MiB [->_____________________________________________________________] 2.85% ? p/s ?3.94 MiB / 97.04 MiB [-->____________________________________________________________] 4.06% ? p/s ?5.65 MiB / 97.04 MiB [-->_______________________________________________] 5.82% 8.04 MiB p/s ETA 11s7.75 MiB / 97.04 MiB [--->______________________________________________] 7.98% 8.04 MiB p/s ETA 11s9.79 MiB / 97.04 MiB [---->____________________________________________] 10.09% 8.04 MiB p/s ETA 10s11.70 MiB / 97.04 MiB [----->__________________________________________] 12.06% 8.18 MiB p/s ETA 10s13.38 MiB / 97.04 MiB [------>_________________________________________] 13.79% 8.18 MiB p/s ETA 10s14.87 MiB / 97.04 MiB [------->________________________________________] 15.32% 8.18 MiB p/s ETA 10s17.06 MiB / 97.04 MiB [-------->________________________________________] 17.58% 8.23 MiB p/s ETA 9s19.14 MiB / 97.04 MiB [--------->_______________________________________] 19.72% 8.23 MiB p/s ETA 9s21.33 MiB / 97.04 MiB [---------->______________________________________] 21.98% 8.23 MiB p/s ETA 9s23.63 MiB / 97.04 MiB [----------->_____________________________________] 24.35% 8.40 MiB p/s ETA 8s25.76 MiB / 97.04 MiB [------------->___________________________________] 26.54% 8.40 MiB p/s ETA 8s28.02 MiB / 97.04 MiB [-------------->__________________________________] 28.87% 8.40 MiB p/s ETA 8s30.15 MiB / 97.04 MiB [--------------->_________________________________] 31.07% 8.56 MiB p/s ETA 7s32.30 MiB / 97.04 MiB [---------------->________________________________] 33.29% 8.56 MiB p/s ETA 7s34.57 MiB / 97.04 MiB [----------------->_______________________________] 35.62% 8.56 MiB p/s ETA 7s35.60 MiB / 97.04 MiB [----------------->_______________________________] 36.69% 8.59 MiB p/s ETA 7s35.85 MiB / 97.04 MiB [------------------>______________________________] 36.95% 8.59 MiB p/s ETA 7s37.57 MiB / 97.04 MiB [------------------>______________________________] 38.72% 8.59 MiB p/s ETA 6s38.77 MiB / 97.04 MiB [------------------->_____________________________] 39.95% 8.38 MiB p/s ETA 6s40.89 MiB / 97.04 MiB [-------------------->____________________________] 42.14% 8.38 MiB p/s ETA 6s43.05 MiB / 97.04 MiB [--------------------->___________________________] 44.36% 8.38 MiB p/s ETA 6s45.31 MiB / 97.04 MiB [---------------------->__________________________] 46.69% 8.54 MiB p/s ETA 6s47.48 MiB / 97.04 MiB [----------------------->_________________________] 48.92% 8.54 MiB p/s ETA 5s49.49 MiB / 97.04 MiB [------------------------>________________________] 50.99% 8.54 MiB p/s ETA 5s51.33 MiB / 97.04 MiB [------------------------->_______________________] 52.89% 8.64 MiB p/s ETA 5s53.30 MiB / 97.04 MiB [-------------------------->______________________] 54.93% 8.64 MiB p/s ETA 5s55.57 MiB / 97.04 MiB [---------------------------->____________________] 57.26% 8.64 MiB p/s ETA 4s57.80 MiB / 97.04 MiB [----------------------------->___________________] 59.56% 8.78 MiB p/s ETA 4s59.67 MiB / 97.04 MiB [------------------------------>__________________] 61.48% 8.78 MiB p/s ETA 4s61.94 MiB / 97.04 MiB [------------------------------->_________________] 63.83% 8.78 MiB p/s ETA 3s64.08 MiB / 97.04 MiB [-------------------------------->________________] 66.03% 8.89 MiB p/s ETA 3s66.31 MiB / 97.04 MiB [--------------------------------->_______________] 68.33% 8.89 MiB p/s ETA 3s68.58 MiB / 97.04 MiB [---------------------------------->______________] 70.67% 8.89 MiB p/s ETA 3s70.42 MiB / 97.04 MiB [----------------------------------->_____________] 72.57% 9.00 MiB p/s ETA 2s72.31 MiB / 97.04 MiB [------------------------------------>____________] 74.52% 9.00 MiB p/s ETA 2s74.33 MiB / 97.04 MiB [------------------------------------->___________] 76.59% 9.00 MiB p/s ETA 2s76.21 MiB / 97.04 MiB [-------------------------------------->__________] 78.53% 9.04 MiB p/s ETA 2s78.44 MiB / 97.04 MiB [--------------------------------------->_________] 80.82% 9.04 MiB p/s ETA 2s80.69 MiB / 97.04 MiB [---------------------------------------->________] 83.14% 9.04 MiB p/s ETA 1s82.83 MiB / 97.04 MiB [----------------------------------------->_______] 85.35% 9.17 MiB p/s ETA 1s84.53 MiB / 97.04 MiB [------------------------------------------>______] 87.11% 9.17 MiB p/s ETA 1s86.76 MiB / 97.04 MiB [------------------------------------------->_____] 89.41% 9.17 MiB p/s ETA 1s87.95 MiB / 97.04 MiB [-------------------------------------------->____] 90.63% 9.12 MiB p/s ETA 0s88.88 MiB / 97.04 MiB [-------------------------------------------->____] 91.59% 9.12 MiB p/s ETA 0s91.12 MiB / 97.04 MiB [---------------------------------------------->__] 93.90% 9.12 MiB p/s ETA 0s92.90 MiB / 97.04 MiB [---------------------------------------------->__] 95.73% 9.07 MiB p/s ETA 0s95.07 MiB / 97.04 MiB [------------------------------------------------>] 97.97% 9.07 MiB p/s ETA 0s96.32 MiB / 97.04 MiB [------------------------------------------------>] 99.26% 9.07 MiB p/s ETA 0s97.04 MiB / 97.04 MiB [----------------------------------------------->] 100.00% 8.93 MiB p/s ETA 0s97.04 MiB / 97.04 MiB [----------------------------------------------->] 100.00% 8.93 MiB p/s ETA 0s97.04 MiB / 97.04 MiB [----------------------------------------------->] 100.00% 8.93 MiB p/s ETA 0s97.04 MiB / 97.04 MiB [----------------------------------------------->] 100.00% 8.35 MiB p/s ETA 0s97.04 MiB / 97.04 MiB [----------------------------------------------->] 100.00% 8.35 MiB p/s ETA 0s97.04 MiB / 97.04 MiB [----------------------------------------------->] 100.00% 8.35 MiB p/s ETA 0s97.04 MiB / 97.04 MiB [----------------------------------------------->] 100.00% 7.81 MiB p/s ETA 0s97.04 MiB / 97.04 MiB [----------------------------------------------->] 100.00% 7.81 MiB p/s ETA 0s97.04 MiB / 97.04 MiB [----------------------------------------------->] 100.00% 7.81 MiB p/s ETA 0s97.04 MiB / 97.04 MiB [----------------------------------------------->] 100.00% 7.31 MiB p/s ETA 0s97.04 MiB / 97.04 MiB [---------------------------------------------------] 100.00% 7.99 MiB p/s 12s2026-06-24T05:48:17Z	INFO	[vulndb] Artifact successfully downloaded	repo="mirror.gcr.io/aquasec/trivy-db:2"
2026-06-24T05:48:17Z	INFO	[vuln] Vulnerability scanning is enabled
2026-06-24T05:48:28Z	INFO	Detected OS	family="debian" version="kali-rolling"
2026-06-24T05:48:28Z	WARN	This OS version is not on the EOL list	family="debian" version="kali-rolling"
2026-06-24T05:48:28Z	INFO	[debian] Detecting vulnerabilities...	os_version="kali-rolling" pkg_num=79
2026-06-24T05:48:28Z	INFO	Number of language-specific files	num=0

Report Summary

┌──────────────────────────────────────────────┬────────┬─────────────────┐
│                    Target                    │  Type  │ Vulnerabilities │
├──────────────────────────────────────────────┼────────┼─────────────────┤
│ kalilinux/kali-rolling (debian kali-rolling) │ debian │        0        │
└──────────────────────────────────────────────┴────────┴─────────────────┘
Legend:
- '-': Not scanned
- '0': Clean (no security findings detected)


```

## What I Learned / Edge Cases / Gotchas
- Cloud tools may need API credentials; container scans work offline with trivy/grype
- Registry template: `trivy image kalilinux/kali-rolling {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 300s

## Next Steps for Exploration & Development
Scan `bkimminich/juice-shop` and `vulnerables/web-dvwa` images directly.

---
*GrokStrike v2 — 2026-06-24T05:48:28.750540+00:00*
