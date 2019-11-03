# All data
class AllData:
    lastJsonData = ''
    lastJsonDataTimestamp = ''

    def hasData(self):
    	return 'global' in self.lastJsonData

    def isOn(self):
    	return int(self.lastJsonData['global']['is_on']['value']) == 1

    def getCadenceMs(self, maxTempoMs):
    	return round(self.lastJsonData['global']['cadence']['value'] * maxTempoMs/100) * 100

    def getMasterMessage(self, currentObjectIndex):
    	intensity = round(self.lastJsonData['enveloppe']['intensity']['value']);
    	attack = round(self.lastJsonData['enveloppe']['attack']['value']);
    	hold = round(self.lastJsonData['enveloppe']['hold']['value']);
    	release = round(self.lastJsonData['enveloppe']['release']['value']);
    	# ID / INTENSITY / ATTACK / HOLD
    	SEPARATOR = " "
    	return "" + str(currentObjectIndex) + SEPARATOR + str(intensity) + SEPARATOR + str(attack) + SEPARATOR + str(hold) + SEPARATOR + str(release) + ""

    # Be careful: it is an integer and not a Boolean (like the JSON file)
    def getIdDescending(self):
    	return int(self.lastJsonData['enveloppe']['id_sort_desc']['value'])

    def getObjectFeature(self):
    	return self.lastJsonData['enveloppe']['id_feature']['value']

    def isSameFeature(self, featureToTest, isIdDescending):
    	# Be carefull of the type is descending. it is integer in JSON and here too
    	#print("{}".format(featureToTest) + "==" + self.getObjectFeature() + " = " + str(self.getObjectFeature() == featureToTest))
    	#print("{}".format(isIdDescending) + "==" + str(self.getIdDescending()) + " = " + str(self.getIdDescending() == isIdDescending))
    	return self.getIdDescending() == isIdDescending and self.getObjectFeature() == featureToTest