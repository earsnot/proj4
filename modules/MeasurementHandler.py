class MeasurementHandler:

	voltageSelectionValue = 0
	currentSelectionValue = 1
	tempSelectionValue = 2

	voltageAvg = 0
	currentAvg = 0
	tempAvg = 0


	def readMeasurements(self):
		# Read and 
		voltageAddress = ADCAddressHandler.getAddress(self.voltageSelectionValue) # Comment: Hvad navn instancierer vi ADCAddressHandler som?
		voltageReading = getMeasurements(voltageAddress) # Pseudo code

		testTing
testTing 2
Tes ting 3


		voltageAvg = DataAverager.average_data(voltageReading) # Comment: Hvad navn instancierer vi average_data for Voltage som?

		voltageAddress = ADCAddressHandler.getAddress(self.voltageSelectionValue) # Comment: Hvad navn instancierer vi ADCAddressHandler som?
		voltageReading = getMeasurements(voltageAddress) # Pseudo code
		voltageAvg = DataAverager.average_data(voltageReading) # Comment: Hvad navn instancierer vi average_data for Voltage som?

		voltageAddress = ADCAddressHandler.getAddress(self.voltageSelectionValue) # Comment: Hvad navn instancierer vi ADCAddressHandler som?
		voltageReading = getMeasurements(voltageAddress) # Pseudo code
		voltageAvg = DataAverager.average_data(voltageReading) # Comment: Hvad navn instancierer vi average_data for Voltage som?

	def getAvgVoltage(self):
		return self.voltageAvg

	def getAvgCurrent(self):
		return self.currentAvg

	def getAvgTemp(self):
		return self.tempAvg