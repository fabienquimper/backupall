import threading
import time 

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
    id = 0
    oscBuilder = None
    lastJsonDataTimestamp = None
    lastJsonData = None

    # parameterized constructor 
    def __init__(self, oscBuilder, lastJsonDataTimestamp, lastJsonData): 
        self.oscBuilder = oscBuilder 
        self.lastJsonDataTimestamp = lastJsonDataTimestamp
        self.lastJsonData = lastJsonData

    def rien(self):
        print("Rien")

    #def filter_min_max(unused_addr, args):
    #    print("Filter min-max: col min max:[{0}] ".format(args))

    #def startOscListenner(self):
        #server.serve_forever()

    def sendOsc(self):
        if self.lastJsonData == '':
            self.lastJsonData = 'empty'
        self.oscBuilder.sendMessage("Toto is here. (OSC message)")

    def action(self):
        print("Run action")
        self.sendOsc()

    def start(self):
        print("Run master")
        #self.startOscListenner()
        inter=setInterval(0.6,self.action)
        # will stop interval in 5s
        #t=threading.Timer(5,inter.cancel)
        #t.start()