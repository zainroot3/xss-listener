#  Custom XSS Cookie Stealer & Listener

A lightweight Python-based HTTP listener designed to bypass **CGNAT** and **Port Forwarding** limitations during XSS (Cross-Site Scripting) attacks. Unlike standard Netcat listeners, this tool provides automatic **Base64 decoding** and handles **CORS headers** for more reliable data exfiltration.

##  Why this tool?
During my penetration testing labs, I noticed that standard listeners like `nc -lvnp` often fail or show warnings when used with tunnels like **Ngrok** behind a CGNAT. 
This tool solves that by:
- **Automatic Decoding:** Instantly decodes `?c=` Base64 parameters (common in XSS payloads).
- **CORS Bypass:** Sends `Access-Control-Allow-Origin: *` headers to ensure the victim's browser doesn't block the request.
- **Stealthy:** Suppresses standard HTTP logging to keep the terminal clean for critical data.

## 🛠️ Installation & Usage

1. **Clone the Repo:**
- git clone https://github.com/zainroot3/xss-listener.git
- python3 xss-listener.py
