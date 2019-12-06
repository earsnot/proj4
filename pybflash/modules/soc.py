class SOC:
	"""Docstring for SOC - Handles estimation of SOC based on start voltage and couloumb counting (current integration)
	Input: dt (time in between interrupts), batteryCapacityInAh"""
	soc = 0

	def __init__(self, dt, battery_capacity_ah):
		self.dt = dt # Defined time in between interrupts
		self.batteryCapacityInC = battery_capacity_ah*3600 # 1Ah = 3600 Coulombs


	def estimate_start_SOC(self, voltageReading): # ((JUST A TESTING FUNCTION - NOT DONE))
		self.soc = voltageReading # Er SOC på grafen fra 0-1 skal der ganges med 100 her.
		if voltageReading < xvalue1:
			self.soc = voltageReading * slope1 + intercept1
			return self.soc
		elif xvalue1 <= voltageReading < xvalue2:
			self.soc = voltageReading * slope2 + intercept2
			return self.soc
		elif xvalue2 <= voltageReading < xvalue3:
			self.soc = voltageReading * slope3 + intercept3
			return self.soc
		elif xvalue3 <= voltageReading < xvalue4:
			self.soc = voltageReading * slope4 + intercept4
			return self.soc

	def esitmate_continuous_SOC(self, currentReading):
		self.soc = self.soc + (currentReading * self.dt * 100) / self.batteryCapacityInC # *100 fordi procent
		return self.soc
