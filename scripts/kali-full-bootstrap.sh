#!/bin/bash
# GrokStrike v2 — full Kali tool bootstrap for local lab documentation
set -e
export DEBIAN_FRONTEND=noninteractive

echo "[GrokStrike] apt update..."
apt-get update -qq

PACKAGES=(
  # Network recon
  nmap masscan nikto sqlmap gobuster feroxbuster dirb wfuzz hydra
  whatweb wafw00f sslscan testssl.sh enum4linux enum4linux-ng smbmap
  netcat-traditional curl wget dnsutils whois theharvester responder
  crackmapexec netexec hping3 traceroute arp-scan nbtscan fierce dnsenum
  dnsrecon rpcclient samba-common-bin
  # Web
  nuclei dirsearch commix tplmap jwt-tool chromium
  # Auth / cracking
  john hashcat medusa patator cewl hash-identifier hashid
  # Binary / RE / forensics
  gdb radare2 binwalk checksec ropper ropgadget binutils file xxd bsdmainutils
  foremost steghide exiftool sleuthkit scalpel testdisk pngcheck zbar-tools
  upx strace ltrace
  # Exploit / framework
  metasploit-framework exploitdb
  # Cloud / container
  trivy docker-bench-security
  # OSINT
  recon-ng spiderfoot sherlock
  # Wordlists
  wordlists seclists
  # Python tooling
  python3-pip python3-venv
)

echo "[GrokStrike] Installing ${#PACKAGES[@]} packages..."
apt-get install -y -qq "${PACKAGES[@]}" 2>/dev/null || true

# pip tools not always in apt
pip3 install --break-system-packages -q \
  arjun paramspider dalfox pwntools volatility3 \
  bloodhound impacket certipy holehe h8mail \
  2>/dev/null || pip3 install -q arjun dalfox pwntools 2>/dev/null || true

# Go-based tools via apt where available, else skip gracefully
for bin in httpx subfinder katana ffuf; do
  apt-get install -y -qq "$bin" 2>/dev/null || echo "[skip] $bin not in apt"
done

# Unpack rockyou if compressed
if [ -f /usr/share/wordlists/rockyou.txt.gz ] && [ ! -f /usr/share/wordlists/rockyou.txt ]; then
  gunzip -k /usr/share/wordlists/rockyou.txt.gz 2>/dev/null || true
fi

# Nuclei templates
nuclei -update-templates -silent 2>/dev/null || true

# Workspace lab artifacts
mkdir -p /workspace /results /workspace/iac
cat > /workspace/hash.txt <<'EOF'
5d41402abc4b2a76b9719d911017c592
098f6bcd4621d373cade4e832627b4f6
EOF
echo 'admin:$1$X$8ZxLJ8ZxLJ8ZxLJ8ZxLJ8.' > /workspace/ntlm.hash 2>/dev/null || true
printf '#!/bin/bash\necho GrokStrike lab binary\n' > /workspace/binary && chmod +x /workspace/binary
echo 'GrokStrike lab metadata file' > /workspace/file
printf '\x89PNG\r\n\x1a\n' > /workspace/image.png
cp /workspace/image.png /workspace/image.jpg 2>/dev/null || touch /workspace/image.jpg
dd if=/dev/zero of=/workspace/disk.img bs=1M count=1 2>/dev/null
dd if=/dev/zero of=/workspace/mem.dump bs=1M count=1 2>/dev/null
dd if=/dev/zero of=/workspace/challenge bs=1M count=1 2>/dev/null
echo 'resource "aws_s3_bucket" "test" { bucket = "grokstrike-lab" }' > /workspace/iac/main.tf

# DVWA auth cookie helper
cat > /workspace/dvwa_login.sh <<'SCRIPT'
#!/bin/bash
# Login to DVWA and emit cookie string for tool use
TARGET="${1:-http://aegis-target}"
JAR=/tmp/dvwa_cookies.txt
rm -f "$JAR"
# Get session + login
curl -sk -c "$JAR" "$TARGET/login.php" -o /dev/null
TOKEN=$(grep -oP 'user_token" value="\K[^"]+' "$TARGET/login.php" 2>/dev/null || curl -sk "$TARGET/login.php" | grep -oP 'user_token" value="\K[^"]+')
curl -sk -b "$JAR" -c "$JAR" -d "username=admin&password=password&Login=Login&user_token=${TOKEN}" "$TARGET/login.php" -o /dev/null
# Set security low
curl -sk -b "$JAR" -c "$JAR" "$TARGET/security.php" -d "security=low&seclev_submit=Submit" -o /dev/null 2>/dev/null || true
# Output cookie header (Netscape cookie format: domain, flag, path, secure, expiry, name, value)
awk 'BEGIN{FS="\t"} NR>1 && NF>=7 {printf "%s=%s;", $6,$7}' "$JAR" | sed 's/;$//'
SCRIPT

# Extended packages (second pass — RE, forensics, exploit, network extras)
apt-get install -y -qq \
  john hashcat radare2 binwalk trivy exploitdb metasploit-framework \
  dirsearch commix steghide exiftool gdb binutils checksec foremost \
  sleuthkit scalpel testdisk pngcheck zbar-tools medusa patator cewl \
  hash-identifier dnsenum fierce arp-scan nbtscan hping3 traceroute \
  enum4linux-ng smbmap netexec xxd strace ltrace 2>/dev/null || true
chmod +x /workspace/dvwa_login.sh

echo "[GrokStrike] Bootstrap complete. Installed tools:"
for t in nmap gobuster sqlmap nuclei nikto feroxbuster ffuf httpx wafw00f dirsearch commix john hashcat radare2 binwalk trivy searchsploit metasploit-framework; do
  which "$t" 2>/dev/null && echo "  OK: $t" || echo "  MISSING: $t"
done
ls -la /usr/share/wordlists/dirb/common.txt 2>/dev/null || ls -la /usr/share/seclists/Discovery/Web-Content/common.txt 2>/dev/null || true