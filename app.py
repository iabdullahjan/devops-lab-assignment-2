from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello! This is Mian Abdullah Jan's Docker container - FA23-BSE-019")

HTTPServer(("", 8080), Handler).serve_forever()
