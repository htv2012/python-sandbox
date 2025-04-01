#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write("Hello, <strong>world</strong>!".encode())


if __name__ == "__main__":
    server = HTTPServer(("", 9001), MyHandler)
    print("Server started on host:{}, port:{}".format(*server.server_address))
    # Serve the page only once then quit
    server.handle_request()
