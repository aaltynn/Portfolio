from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import sys

# Change to the directory where static files are located
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class MyHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        super().end_headers()

    def do_GET(self):
        # Serve index.html for root path
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()

# Get port from environment or default to 8000
port = int(os.environ.get('PORT', 8000))
server_address = ('0.0.0.0', port)
httpd = HTTPServer(server_address, MyHTTPRequestHandler)

print(f"Server running on port {port}...")
httpd.serve_forever()
