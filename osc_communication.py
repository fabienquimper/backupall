from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import udp_client
from pythonosc import osc_message_builder
import threading

class OscDispatcher():
    dispatcher = None

    def print_objects(self, unused_addr, args):
        print("Data (OSC message received): " + args)
        #print("Mode received: [{0}]".format(args[0]))

    def createVideoSlave(self):
        self.dispatcher = dispatcher.Dispatcher()
        self.dispatcher.map("/video/shape", self.print_objects)
        return self.dispatcher

    def createLightSlave(self):
        self.dispatcher = dispatcher.Dispatcher()
        self.dispatcher.map("/light/shape", self.print_objects)
        return self.dispatcher

    def createAudioSlave(self):
        self.dispatcher = dispatcher.Dispatcher()
        self.dispatcher.map("/audio/shape", self.print_objects)
        return self.dispatcher


# This class prepare a OSC client
# OSC server (to receive message for Test Purpose) in a thread
class OscCommunication():
    client = None
    serverOsc = None
    thread = None
    # OSC caracteristic
    uri = None
    port = None
    dispatcher = None

    # parameterized constructor 
    def __init__(self, uri, port, dispatcher): 
        self.uri = uri 
        self.port = port
        self.dispatcher = dispatcher

    def start(self):
        self.client = udp_client.SimpleUDPClient(self.uri, self.port)
        #self.dispatcher = dispatcher.Dispatcher()
        #self.dispatcher.map("/audio/shape", self.print_objects)#filter_min_max  rien
        #self.serverOsc = osc_server.ThreadingOSCUDPServer((self.uri, self.port), self.dispatcher)
        #self.thread = threading.Thread(target = self.serverOsc.serve_forever)
        #self.thread.start()

    def sendAudioMessage(self, msg):
        head_message = "/audio/shape"
        print("OSC message send is: '" + head_message + msg + "'")
        self.client.send_message(head_message, msg)
        #client.send_message("/control/controler/sequence", lastJsonData)
        #client.send_message("/control/controler/sequence", lastJsonDataTimestamp)
