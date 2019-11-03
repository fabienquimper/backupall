import threading
import time
import json
import datajson
from dataobj import getAllObjectsByFeature
import random

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
    currentObjectIndex = 0
    currentObjectList = getAllObjectsByFeature('id', 0)#random.shuffle([i for i in range(1001)])
    currentObjectFeature = 'id'
    currentObjectSortDescending = 0
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
        infoOsc = ''
        if self.allData.hasData():
            currentOjbectId = 0
            try:
                currentOjbectId = int(self.currentObjectList.iloc[self.currentObjectIndex, :].loc['id'])
            except:
                print("An exception occurred on currentOjbectId") 
            print("Current id of index '" + "{}".format(self.currentObjectIndex) + "' is : '" + "{}".format(currentOjbectId) +"'" )
            infoOsc = self.allData.getMasterMessage(currentOjbectId)
            #self.oscBuilder.sendMessage("Toto is here. (OSC message) " + infoOsc)
            self.oscBuilder.sendAudioMessage(infoOsc)

    def updateTimerStatus(self):
        global LAST_ACTION_DURATION
        global TEMPO
        global TECHNICAL_TEMPO_MILLISECONDS

        #print(self.allData.lastJsonData)

        if self.allData.hasData():
            cadence = self.allData.getCadenceMs(MAX_TEMPO_MS)
            print("Current CADENCE: " + "{}".format(cadence));
            if TEMPO != cadence:
                TEMPO = cadence
                print("Updated CADENCE to " + "{}".format(TEMPO));

        # Manage OFF
        if not self.allData.hasData() or not self.allData.isOn():
            print("Currently OFF or not data receive.")
            return

        print("Run updateTimerStatus " + "{}".format(TECHNICAL_TEMPO_MILLISECONDS) + " ms - Last action was since: " + "{}".format(LAST_ACTION_DURATION) + "ms (tempo = " + "{}".format(TEMPO) + "ms)")
        if LAST_ACTION_DURATION == -1 or LAST_ACTION_DURATION >= TEMPO:
            print("ACTION IS COMING" + "{}".format(LAST_ACTION_DURATION) + " ms")
            # Do action
            LAST_ACTION_DURATION = 0
            # If the action is not the same the index is reset
            if self.allData.hasData() and not self.allData.isSameFeature(self.currentObjectFeature, self.currentObjectSortDescending):
                print("Feature are updated **")
                self.currentObjectIndex = 0
                self.currentObjectFeature = self.allData.getObjectFeature()
                self.currentObjectSortDescending = self.allData.getIdDescending()
                self.currentObjectList = getAllObjectsByFeature(self.currentObjectFeature, not self.currentObjectSortDescending)
            else:
                print("Go to the next object " + str(self.currentObjectIndex) + " **")
                self.currentObjectIndex = (self.currentObjectIndex + 1) % 1000
            # Send OSC message
            self.sendOsc()

        else:
            LAST_ACTION_DURATION = LAST_ACTION_DURATION + TECHNICAL_TEMPO_MILLISECONDS

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