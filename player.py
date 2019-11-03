import threading
import time
import json
import datajson

MAX_TEMPO_MS = 20000

TECHNICAL_TEMPO_MILLISECONDS = 100
LAST_ACTION_DURATION = -1
#LAST_ACTION_TIMESTAMP = -1
TEMPO = 1500
#LAST_TEMPO = TEMPO

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
    allData = None
    #lastJsonDataTimestamp = None
    #lastJsonData = None

    # parameterized constructor 
    def __init__(self, oscBuilder, allData): 
        self.oscBuilder = oscBuilder 
        #self.lastJsonDataTimestamp = lastJsonData.lastJsonDataTimestamp
        #self.lastJsonData = lastJsonData.lastJsonData
        self.allData = allData

    def rien(self):
        print("Rien")

    #def filter_min_max(unused_addr, args):
    #    print("Filter min-max: col min max:[{0}] ".format(args))

    #def startOscListenner(self):
        #server.serve_forever()

    def sendOsc(self):
        #if self.lastJsonData == '':
        #    self.lastJsonData = 'empty'
        self.oscBuilder.sendMessage("Toto is here. (OSC message)")

    def updateTimerStatus(self):
        global LAST_ACTION_DURATION
        global TEMPO
        global TECHNICAL_TEMPO_MILLISECONDS

        #print(self.allData.lastJsonData)

        if self.allData.hasData():
            cadence = self.allData.getCadenceMs(MAX_TEMPO_MS)
            #cadence = round(self.allData.lastJsonData['global']['cadence']['value'] * MAX_TEMPO_MS/100) * 100
            print("Current CADENCE: " + "{}".format(cadence));
            if TEMPO != cadence:
                TEMPO = cadence
                print("Updated CADENCE to " + "{}".format(TEMPO));
        #print("Updated CADENCE: " + self.lastJsonData['global']['cadence']['value']);

        print("Run updateTimerStatus " + "{}".format(TECHNICAL_TEMPO_MILLISECONDS) + " ms - Last action was since: " + "{}".format(LAST_ACTION_DURATION) + "ms (tempo = " + "{}".format(TEMPO) + "ms)")
        if LAST_ACTION_DURATION == -1 or LAST_ACTION_DURATION >= TEMPO:
            print("ACTION IS COMING" + "{}".format(LAST_ACTION_DURATION) + " ms")
            # Do action
            self.sendOsc()
            LAST_ACTION_DURATION = 0
        else:
            if self.allData.hasData() and self.allData.isOn():
                LAST_ACTION_DURATION = LAST_ACTION_DURATION + TECHNICAL_TEMPO_MILLISECONDS
            else:
                print("Currently OFF")
        #TECHNICAL_TEMPO_MILLISECONDS = 100
        #LAST_ACTION_DURATION = -1
        #TEMPO = 1500
        #LAST_TEMPO = TEMPO

    def action(self):
        self.updateTimerStatus()

    def start(self):
        global TECHNICAL_TEMPO_MILLISECONDS
        print("Run master")
        #self.startOscListenner()
        inter=setInterval(TECHNICAL_TEMPO_MILLISECONDS/1000.0,self.action)
        # will stop interval in 5s
        #t=threading.Timer(5,inter.cancel)
        #t.start()