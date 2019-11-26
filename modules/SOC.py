BATTERY_CAPACITY = 18 # Ah (Amp-hours)

class SOC:
	"""Docstring for SOC - Handles estimation of SOC based on start voltage and couloumb counting (current integration)
	Input: dt (time in between interrupts), batteryCapacityInAh"""
	SOC = 0

	def __init__(self, dt, battery_capacity_ah):
		self.dt = dt # Defined time in between interrupts
		self.batteryCapacityInC = battery_capacity_ah*3600 # 1Ah = 3600 Coulombs


	def estimate_start_SOC(self, voltageReading, testConstant): # ((JUST A TESTING FUNCTION - NOT DONE))
		self.SOC = voltageReading * testConstant # Er SOC på grafen fra 0-1 skal der ganges med 100 her.
		return self.SOC


	def esitmate_continuous_SOC(self, currentReading):
		self.SOC = self.SOC + (currentReading * self.dt * 100) / self.batteryCapacityInC # *100 fordi procent
		return self.SOC

# --------------- TEST ------------------
SOCtest = SOC(1, 13.889) # dt = 1 sekund, capacitet = 13.889 Ah = ~50000 Couloumb 
print(SOCtest.estimate_start_SOC(50,0.01)) # Voltage = 50V, factor = 0.01 -- start SOC = 0.5
print(SOCtest.esitmate_continuous_SOC(50000/2)) # Current = 25000A for 1 second = 25000 couloumbs (Final SOC should be 1!)
