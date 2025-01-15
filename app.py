
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

# Define the host and port
HOST = "0.0.0.0"  # Listen on all available interfaces
PORT = 8080       # Use port 8080

# Create a simple HTTP server
class Handler(SimpleHTTPRequestHandler):
    pass

with TCPServer((HOST, PORT), Handler) as httpd:
    print(f"Serving on http://{HOST}:{PORT}")
    httpd.serve_forever()

