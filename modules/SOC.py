class SOC:
	"""Docstring for SOC - Handles estimation of SOC based on start voltage and couloumb counting (current integration)
	Input: dt (time in between interrupts), batteryCapacityInAh"""
	SOC = 0

	def __init__(self, dt, battery_capacity_ah):
		self.dt = dt # Defined time in between interrupts
		self.batteryCapacityInC = battery_capacity_ah*3600 # 1Ah = 3600 Coulombs


	def estimate_start_SOC(self, voltage_reading, testConstant): # ((JUST A TESTING FUNCTION - NOT DONE))
		self.SOC = voltageReading * testConstant # Er SOC på grafen fra 0-1 skal der ganges med 100 her.
		return self.SOC


	def estitmate_continuous_SOC(self, currentReading):
		self.SOC = self.SOC + (currentReading * self.dt * 100) / self.batteryCapacityInC # *100 fordi procent
		return self.SOC