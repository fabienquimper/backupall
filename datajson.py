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