import http.server
import socketserver

PORT=8890
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("server is running at ", PORT)
    print("to test from dockerized  version, please run ....")
    httpd.serve_forever()
