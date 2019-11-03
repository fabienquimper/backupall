import http.server
import threading
import time 
import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler, CGIHTTPRequestHandler
import json
import datetime

def getDateTimestamp():
    return datetime.datetime.fromtimestamp(time.gmtime()).isoformat()

class S(CGIHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def _html(self, message):
        """This just generates an HTML document that includes `message`
        in the body. Override, or re-write this do do more interesting stuff.
        """
        content = f"<html><body><h1>{message}</h1></body></html>"
        return content.encode("utf8")  # NOTE: must return a bytes object!

    #def do_GET(self):
        #        if self.path.startswith('/view/'):
        #    return self.get_view()
    #    self._set_headers()
    #    self.wfile.write(self._html("hi!"))
    #    print("GET !!!!")

    def do_HEAD(self):
        print("HEAD !!!!")
        self._set_headers()

    def do_POST(self):
        print("POST !!!!")
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        print(post_body)
        global jsonDataReceived
        global lastJsonDataTimestamp
        jsonDataReceived = json.loads( post_body )
        print(jsonDataReceived)
        lastJsonDataTimestamp = getDateTimestamp
        print(lastJsonDataTimestamp)
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write(self._html("POST!"))

def run(server_class=HTTPServer, handler_class=S, addr="localhost", port=7000):
    server_address = ("", port)

    server = http.server.HTTPServer
    handler = S#http.server.CGIHTTPRequestHandler
    handler.cgi_directories = ["/index.html"]
    print("Serveur actif sur le port :", port)

    httpd = server(server_address, handler)

    print("Before")
    thread1 = threading.Thread(target = httpd.serve_forever)
    thread1.start()
    #thread1.join()

StartTime=time.time()