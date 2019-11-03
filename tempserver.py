import http.server
import threading
import time 
import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler, CGIHTTPRequestHandler
import json
import datetime
#from pythonosc import dispatcher
#from pythonosc import osc_server
#from pythonosc import udp_client

global lastJsonData
global lastJsonDataTimestamp

def rien():
    print("Rien")

#client = udp_client.SimpleUDPClient("localhost", "8001")

#dispatcher = dispatcher.Dispatcher()
#dispatcher.map("/control/controler/filter/min-max", rien)#filter_min_max
#server = osc_server.ThreadingOSCUDPServer(("localhost", "8001"), dispatcher)
#thread2 = threading.Thread(target = server.serve_forever)
#thread2.start()

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
        jsonDataReceived = json.loads( post_body )
        print(jsonDataReceived)
        lastJsonDataTimestamp = getDateTimestamp
        print(lastJsonDataTimestamp)
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write(self._html("POST!"))

StartTime=time.time()

class setInterval :
    def __init__(self,interval,action) :
        self.interval=interval
        self.action=action
        self.stopEvent=threading.Event()
        thread=threading.Thread(target=self.__setInterval)
        thread.start()

    def __setInterval(self) :
        nextTime=time.time()+self.interval
        while not self.stopEvent.wait(nextTime-time.time()) :
            nextTime+=self.interval
            self.action()

    def cancel(self) :
        self.stopEvent.set()

class PlayerMaster:
    def rien():
        print("Rien")

    #def filter_min_max(unused_addr, args):
    #    print("Filter min-max: col min max:[{0}] ".format(args))

    #def startOscListenner(self):
        #server.serve_forever()


    def sendOsc(self):
        client.send_message("/control/controler/filter/min-max", "alt")

    def action(self):
        print("Run action")
        #self.sendOsc()

    def start(self):
        print("Run master")
        #self.startOscListenner()
        inter=setInterval(0.6,self.action)
        # will stop interval in 5s
        #t=threading.Timer(5,inter.cancel)
        #t.start()


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


def waitForever():
    print("After")
    while True:
        time.sleep(1)
    print("End")

def runMaster():
    player = PlayerMaster()
    player.start()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Run a simple HTTP server")
    parser.add_argument(
        "-l",
        "--listen",
        default="localhost",
        help="Specify the IP address on which the server listens",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=7000,
        help="Specify the port on which the server listens",
    )
    args = parser.parse_args()

    print("Before run")

    # Run the webserver
    run(addr=args.listen, port=args.port)

    # Run master
    runMaster()

    # Start forever loops
    #waitForever()

