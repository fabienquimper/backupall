#import http.server
#import threading
#import time 
import argparse
#from http.server import HTTPServer, BaseHTTPRequestHandler, CGIHTTPRequestHandler
#import json
#import datetime
#from pythonosc import dispatcher
#from pythonosc import osc_server
#from pythonosc import udp_client
#from pythonosc import osc_message_builder

# Own module
from osc_communication import OscDispatcher, OscCommunication
import webserver
import player
import dataobj

# All data
lastJsonData = ''
lastJsonDataTimestamp = ''

# OSC module
oscDispatcher = OscDispatcher()
oscBuilder = OscCommunication("127.0.0.1", 8001, oscDispatcher.createVideoSlave())
oscBuilder.start()

def waitForever():
    print("After")
    while True:
        time.sleep(1)
    print("End")

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
    webserver.run(addr=args.listen, port=args.port)

    # Run master
    #global oscBuilder
    #global lastJsonData
    #global lastJsonDataTimestamp
    player = player.PlayerMaster(oscBuilder, lastJsonData, lastJsonDataTimestamp)
    player.start()

    # Start forever loops
    #waitForever()

