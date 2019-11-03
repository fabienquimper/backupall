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
    	intensity = round(self.lastJsonData['enveloppe']['intensity']['value'] * 100);
    	attack = round(self.lastJsonData['enveloppe']['attack']['value'] * 100);
    	hold = round(self.lastJsonData['enveloppe']['hold']['value'] * 100);
    	release = round(self.lastJsonData['enveloppe']['release']['value'] * 100);
    	# ID / INTENSITY / ATTACK / HOLD
    	return "/" + str(currentObjectIndex) + "/" + str(intensity) + "/" + str(attack) + "/" + str(hold) + "/" + str(release)

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