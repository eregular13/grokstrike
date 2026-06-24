# wfuzz

## Tool Name & Category
| Field | Value |
|-------|-------|
| **Category** | web — Web Application Security |
| **Binary** | `wfuzz` ✅ installed |
| **Agent** | web |
| **DVWA-optimized** | True |
| **Lab target** | `http://aegis-target` |

## Official Purpose
Web fuzzer

## Exact Command(s) Executed
```bash
# SAFETY CHECK PASSED — local Docker lab only (DVWA + Juice Shop)
wfuzz -c -z file,/usr/share/wordlists/dirb/common.txt --hc 404,500 -t 10 http://aegis-target/FUZZ
```

| Metric | Value |
|--------|-------|
| Duration | 2.02s |
| Exit code | 0 |
| Effectiveness | **9/10** — Rich actionable output |

## Key Findings
- **Potential vulnerability signal:** sql
- **Potential vulnerability signal:** sql
- **Potential vulnerability signal:** sql
- **Potential vulnerability signal:** sql
- **Potential vulnerability signal:** sql
- **Potential vulnerability signal:** injection
- **Potential vulnerability signal:** sql
- **Potential vulnerability signal:** sql

## Full Output Summary
```
default
default
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://aegis-target/FUZZ
Total requests: 4614

=====================================================================
ID        [0m   Response[0m   Lines [0m   Word    [0m   Chars    [0m   Payload        [0m

=====================================================================

000000001:[0m   [34m302     [0m   0 L   [0m   0 W     [0m   0 Ch     [0m   "http://aegis-t[0m

          [0m   [34m        [0m         [0m           [0m            [0m   arget/"        [0m

000000048:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   284 Ch   [0m   "_derived"     [0m


[0K[1A
[0K000000031:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   282 Ch   [0m   "_admin"       [0m


[0K[1A
[0K000000046:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   285 Ch   [0m   "_database"    [0m


[0K[1A
[0K000000007:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   286 Ch   [0m   ".cvsignore"   [0m


[0K[1A
[0K000000050:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   282 Ch   [0m   "_dummy"       [0m


[0K[1A
[0K000000047:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   287 Ch   [0m   "_db_backups"  [0m


[0K[1A
[0K000000003:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   283 Ch   [0m   ".bashrc"      [0m


[0K[1A
[0K000000049:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   280 Ch   [0m   "_dev"         [0m


[0K[1A
[0K000000015:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   285 Ch   [0m   ".listings"    [0m


[0K[1A
[0K000000045:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   281 Ch   [0m   "_data"        [0m


[0K[1A
[0K000000044:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   280 Ch   [0m   "_css"         [0m


[0K[1A
[0K000000043:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   283 Ch   [0m   "_config"      [0m


[0K[1A
[0K000000038:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   282 Ch   [0m   "_cache"       [0m


[0K[1A
[0K000000040:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   281 Ch   [0m   "_code"        [0m


[0K[1A
[0K000000042:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   281 Ch   [0m   "_conf"        [0m


[0K[1A
[0K000000041:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   283 Ch   [0m   "_common"      [0m


[0K[1A
[0K000000036:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   281 Ch   [0m   "_baks"        [0m


[0K[1A
[0K000000039:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   285 Ch   [0m   "_catalogs"    [0m


[0K[1A
[0K000000037:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   284 Ch   [0m   "_borders"     [0m


[0K[1A
[0K000000035:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   283 Ch   [0m   "_backup"      [0m


[0K[1A
[0K000000034:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   283 Ch   [0m   "_assets"      [0m


[0K[1A
[0K000000033:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   284 Ch   [0m   "_archive"     [0m


[0K[1A
[0K000000027:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   280 Ch   [0m   ".web"         [0m


[0K[1A
[0K000000029:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   277 Ch   [0m   "_"            [0m


[0K[1A
[0K000000030:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   280 Ch   [0m   "_adm"         [0m


[0K[1A
[0K000000025:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   288 Ch   [0m   ".svn/entries" [0m


[0K[1A
[0K000000026:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   280 Ch   [0m   ".swf"         [0m


[0K[1A
[0K000000028:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   277 Ch   [0m   "@"            [0m


[0K[1A
[0K000000032:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   281 Ch   [0m   "_ajax"        [0m


[0K[1A
[0K000000024:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   280 Ch   [0m   ".svn"         [0m


[0K[1A
[0K000000018:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   281 Ch   [0m   ".perf"        [0m


[0K[1A
[0K000000021:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   287 Ch   [0m   ".sh_history"  [0m


[0K[1A
[0K000000019:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   284 Ch   [0m   ".profile"     [0m


[0K[1A
[0K000000017:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   283 Ch   [0m   ".passwd"      [0m


[0K[1A
[0K000000020:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   283 Ch   [0m   ".rhosts"      [0m


[0K[1A
[0K000000023:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   287 Ch   [0m   ".subversion"  [0m


[0K[1A
[0K000000014:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   284 Ch   [0m   ".listing"     [0m


[0K[1A
[0K000000022:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   280 Ch   [0m   ".ssh"         [0m


[0K[1A
[0K000000016:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   290 Ch   [0m   ".mysql_history[0m

          [0m   [31m        [0m         [0m           [0m            [0m   "              [0m


[0K[1A
[0K[1A
[0K000000013:[0m   [31m403     [0m   11 L  [0m   32 W    [0m   296 Ch   [0m   ".htpasswd"    [0m

000000012:[0m   [31m403     [0m   11 L  [0m   32 W    [0m   296 Ch   [0m   ".htaccess"    [0m

000000011:[0m   [31m403     [0m   11 L  [0m   32 W    [0m   291 Ch   [0m   ".hta"         [0m

000000005:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   283 Ch   [0m   ".config"      [0m


[0K[1A
[0K000000006:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   280 Ch   [0m   ".cvs"         [0m


[0K[1A
[0K000000010:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   284 Ch   [0m   ".history"     [0m


[0K[1A
[0K000000008:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   284 Ch   [0m   ".forward"     [0m


[0K[1A
[0K000000002:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   289 Ch   [0m   ".bash_history"[0m


[0K[1A
[0K000000009:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   285 Ch   [0m   ".git/HEAD"    [0m


[0K[1A
[0K000000004:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   282 Ch   [0m   ".cache"       [0m


[0K[1A
[0K000000051:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   282 Ch   [0m   "_files"       [0m


[0K[1A
[0K000000053:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   284 Ch   [0m   "_fpclass"     [0m


[0K[1A
[0K000000057:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   284 Ch   [0m   "_include"     [0m


[0K[1A
[0K000000096:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   294 Ch   [0m   "_vti_bin/shtml[0m

          [0m   [31m        [0m         [0m           [0m            [0m   .dll"          [0m


[0K[1A
[0K[1A
[0K000000097:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   284 Ch   [0m   "_vti_cnf"     [0m


[0K[1A
[0K000000098:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   284 Ch   [0m   "_vti_inf"     [0m


[0K[1A
[0K000000100:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   284 Ch   [0m   "_vti_map"     [0m


[0K[1A
[0K000000065:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   279 Ch   [0m   "_mm"          [0m


[0K[1A
[0K000000099:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   284 Ch   [0m   "_vti_log"     [0m


[0K[1A
[0K000000081:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   282 Ch   [0m   "_stats"       [0m


[0K[1A
[0K000000095:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   304 Ch   [0m   "_vti_bin/_vti_[0m

          [0m   [31m        [0m         [0m           [0m            [0m   aut/author.dll"[0m


[0K[1A
[0K[1A
[0K000000094:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   303 Ch   [0m   "_vti_bin/_vti_[0m

          [0m   [31m        [0m         [0m           [0m            [0m   adm/admin.dll" [0m


[0K[1A
[0K[1A
[0K000000093:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   284 Ch   [0m   "_vti_bin"     [0m


[0K[1A
[0K000000088:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   281 Ch   [0m   "_test"        [0m


[0K[1A
[0K000000090:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   280 Ch   [0m   "_tmp"         [0m


[0K[1A
[0K000000092:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   284 Ch   [0m   "_vti_aut"     [0m


[0K[1A
[0K000000089:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   283 Ch   [0m   "_themes"      [0m


[0K[1A
[0K000000091:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   286 Ch   [0m   "_tmpfileop"   [0m


[0K[1A
[0K000000087:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   286 Ch   [0m   "_templates"   [0m


[0K[1A
[0K000000086:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   285 Ch   [0m   "_template"    [0m


[0K[1A
[0K000000085:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   287 Ch   [0m   "_tempalbums"  [0m


[0K[1A
[0K000000084:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   281 Ch   [0m   "_temp"        [0m


[0K[1A
[0K000000083:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   280 Ch   [0m   "_swf"         [0m


[0K[1A
[0K000000077:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   290 Ch   [0m   "_scriptlibrary[0m

          [0m   [31m        [0m         [0m           [0m            [0m   "              [0m


[0K[1A
[0K[1A
[0K000000079:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   283 Ch   [0m   "_source"      [0m


[0K[1A
[0K000000076:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   286 Ch   [0m   "_resources"   [0m


[0K[1A
[0K000000075:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   280 Ch   [0m   "_res"         [0m


[0K[1A
[0K000000080:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   280 Ch   [0m   "_src"         [0m


[0K[1A
[0K000000078:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   284 Ch   [0m   "_scripts"     [0m


[0K[1A
[0K000000082:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   283 Ch   [0m   "_styles"      [0m


[0K[1A
[0K000000074:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   284 Ch   [0m   "_reports"     [0m


[0K[1A
[0K000000073:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   284 Ch   [0m   "_private"     [0m


[0K[1A
[0K000000072:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   282 Ch   [0m   "_pages"       [0m


[0K[1A
[0K000000067:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   286 Ch   [0m   "_mygallery"   [0m


[0K[1A
[0K000000069:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   282 Ch   [0m   "_notes"       [0m


[0K[1A
[0K000000071:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   284 Ch   [0m   "_overlay"     [0m


[0K[1A
[0K000000068:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   280 Ch   [0m   "_net"         [0m


[0K[1A
[0K000000070:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   280 Ch   [0m   "_old"         [0m


[0K[1A
[0K000000064:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   284 Ch   [0m   "_mem_bin"     [0m


[0K[1A
[0K000000066:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   292 Ch   [0m   "_mmserverscrip[0m

          [0m   [31m        [0m         [0m           [0m            [0m   ts"            [0m


[0K[1A
[0K[1A
[0K000000063:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   282 Ch   [0m   "_media"       [0m


[0K[1A
[0K000000062:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   280 Ch   [0m   "_lib"         [0m


[0K[1A
[0K000000061:[0m   [31m404     [0m   9 L   [0m   32 W    [0m   284 Ch   [0m   "_layouts"     [0m


[0K[1A
[0K000000055:[0m   [
```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab
- Registry template: `wfuzz -c -z file,/usr/share/wordlists/dirb/common.txt --hc 404 {web}/FUZZ {extra}`

## Recommended Safe Parameters for Learning Labs
- Scope: `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) only
- From Kali network: `aegis-target`, `aegis-juice`
- DVWA login: `admin` / `password` — use `/workspace/dvwa_login.sh` for cookie-aware tools
- Suggested timeout: 120s

## Next Steps for Exploration & Development
Run `wfuzz --help` and tune `wfuzz -c -z file,/usr/share/wordlists/dirb/common.txt --hc 404 {web}/FUZZ {extra}` for your target.

---
*GrokStrike v2 — 2026-06-24T05:47:36.656597+00:00*
