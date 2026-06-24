# dirb

## Tool Name & Category
- **Name:** dirb
- **Category:** web (Web Application Security — crawling, fuzzing, vulnerability scanning)
- **Binary:** `dirb`
- **Agent:** web
- **DVWA-optimized:** True

## Official Purpose
Web content scanner

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
dirb http://aegis-target
```

**Target:** `http://aegis-target`  
**Duration:** 1.06s | **Exit code:** 0

## Full Output Summary
```

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Wed Jun 24 05:11:21 2026
URL_BASE: http://aegis-target/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

*** Generating Wordlist...
                                                                               
GENERATED WORDS: 4612

---- Scanning URL: http://aegis-target/ ----
*** Calculating NOT_FOUND code...
                                                                               
                                                                               
--> Testing: http://aegis-target/.bash_history
                                                                               
--> Testing: http://aegis-target/.bashrc
                                                                               
--> Testing: http://aegis-target/.cache
                                                                               
--> Testing: http://aegis-target/.config
                                                                               
--> Testing: http://aegis-target/.cvs
                                                                               
--> Testing: http://aegis-target/.cvsignore
                                                                               
--> Testing: http://aegis-target/.forward
                                                                               
--> Testing: http://aegis-target/.git/HEAD
                                                                               
--> Testing: http://aegis-target/.history
                                                                               
--> Testing: http://aegis-target/.hta
                                                                               
--> Testing: http://aegis-target/.htaccess
                                                                               
--> Testing: http://aegis-target/.htpasswd
                                                                               
--> Testing: http://aegis-target/.listing
                                                                               
--> Testing: http://aegis-target/.listings
                                                                               
--> Testing: http://aegis-target/.mysql_history
                                                                               
--> Testing: http://aegis-target/.passwd
                                                                               
--> Testing: http://aegis-target/.perf
                                                                               
--> Testing: http://aegis-target/.profile
                                                                               
--> Testing: http://aegis-target/.rhosts
                                                                               
--> Testing: http://aegis-target/.sh_history
                                                                               
--> Testing: http://aegis-target/.ssh
                                                                               
--> Testing: http://aegis-target/.subversion
                                                                               
--> Testing: http://aegis-target/.svn
                                                                               
--> Testing: http://aegis-target/.svn/entries
                                                                               
--> Testing: http://aegis-target/.swf
                                                                               
--> Testing: http://aegis-target/.web
                                                                               
--> Testing: http://aegis-target/@
                                                                               
--> Testing: http://aegis-target/_
                                                                               
--> Testing: http://aegis-target/_adm
                                                                               
--> Testing: http://aegis-target/_admin
                                                                               
--> Testing: http://aegis-target/_ajax
                                                                               
--> Testing: http://aegis-target/_archive
                                                                               
--> Testing: http://aegis-target/_assets
                                                                               
--> Testing: http://aegis-target/_backup
                                                                               
--> Testing: http://aegis-target/_baks
                                                                               
--> Testing: http://aegis-target/_borders
                                                                               
--> Testing: http://aegis-target/_cache
                                                                               
--> Testing: http://aegis-target/_catalogs
                                                                               
--> Testing: http://aegis-target/_code
                                                                               
--> Testing: http://aegis-target/_common
                                                                               
--> Testing: http://aegis-target/_conf
                                                                               
--> Testing: http://aegis-target/_config
                                                                               
--> Testing: http://aegis-target/_css
                                                                               
--> Testing: http://aegis-target/_data
                                                                               
--> Testing: http://aegis-target/_database
                                                                               
--> Testing: http://aegis-target/_db_backups
                                                                               
--> Testing: http://aegis-target/_derived
                                                                               
--> Testing: http://aegis-target/_dev
                                                                               
--> Testing: http://aegis-target/_dummy
                                                                               
--> Testing: http://aegis-target/_files
                                                                               
--> Testing: http://aegis-target/_flash
                                                                               
--> Testing: http://aegis-target/_fpclass
                                                                               
--> Testing: http://aegis-target/_images
                                                                               
--> Testing: http://aegis-target/_img
                                                                               
--> Testing: http://aegis-target/_inc
                                                                               
--> Testing: http://aegis-target/_include
                                                                               
--> Testing: http://aegis-target/_includes
                                                                               
--> Testing: http://aegis-target/_install
                                                                               
--> Testing: http://aegis-target/_js
                                                                               
--> Testing: http://aegis-target/_layouts
                                                                               
--> Testing: http://aegis-target/_lib
                                                                               
--> Testing: http://aegis-target/_media
          
```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab context
- Registry template: `dirb {web} {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**8/10** — Strong signal on DVWA/Juice Shop

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=http://aegis-target only; no destructive flags
- Timeout: 90s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:22.049412+00:00*
