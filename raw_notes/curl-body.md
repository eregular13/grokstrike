# curl-body

## Tool Name & Category
- **Name:** curl-body
- **Category:** web (Web Application Security — crawling, fuzzing, vulnerability scanning)
- **Binary:** `curl`
- **Agent:** web
- **DVWA-optimized:** True

## Official Purpose
Fetch page body

## Exact Command(s) Executed
```bash
# Safety check: read-only/lab-safe against local Docker targets only
curl -skL http://aegis-target
```

**Target:** `http://aegis-target`  
**Duration:** 0.11s | **Exit code:** 0

## Full Output Summary
```

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">

	<head>

		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />

		<title>Login :: Damn Vulnerable Web Application (DVWA) v1.10 *Development*</title>

		<link rel="stylesheet" type="text/css" href="dvwa/css/login.css" />

	</head>

	<body>

	<div id="wrapper">

	<div id="header">

	<br />

	<p><img src="dvwa/images/login_logo.png" /></p>

	<br />

	</div> <!--<div id="header">-->

	<div id="content">

	<form action="login.php" method="post">

	<fieldset>

			<label for="user">Username</label> <input type="text" class="loginInput" size="20" name="username"><br />


			<label for="pass">Password</label> <input type="password" class="loginInput" AUTOCOMPLETE="off" size="20" name="password"><br />

			<br />

			<p class="submit"><input type="submit" value="Login" name="Login"></p>

	</fieldset>

	<input type='hidden' name='user_token' value='0bfac22fc4bb9345f6e88b16bffbec52' />

	</form>

	<br />

	

	<br />
	<br />
	<br />
	<br />
	<br />
	<br />
	<br />
	<br />

	<!-- <img src="dvwa/images/RandomStorm.png" /> -->
	</div > <!--<div id="content">-->

	<div id="footer">

	<p><a href="http://www.dvwa.co.uk/" target="_blank">Damn Vulnerable Web Application (DVWA)</a></p>

	</div> <!--<div id="footer"> -->

	</div> <!--<div id="wrapper"> -->

	</body>

</html>
```

## What I Learned / Edge Cases / Gotchas
- Executed successfully in isolated lab context
- Registry template: `curl -skL {web} {extra}`
- Tags: none

## Effectiveness on This Target (1-10)
**8/10** — Strong signal on DVWA/Juice Shop

## Recommended Safe Parameters for Learning Labs
- --batch --risk=1 --level=1 for injection tools; -T4 for nmap; target=http://aegis-target only; no destructive flags
- Timeout: 30s (capped for batch run)
- Always scope to `localhost:8080` (DVWA) or `localhost:3000` (Juice Shop) from host
- Use `aegis-target` / `aegis-juice` hostnames from inside Kali container network

---
*GrokStrike v1.0 — 2026-06-24T05:11:26.535881+00:00*
