class SOC:
	"""docstring for SOC - Handles estimation of SOC based on start voltage and couloumb counting (current integration)
	Input = dt (1/interrupt frequency), totalCapacity (in aH)"""
	SOC = 0

	def __init__(self, dt, batteryCapacityInAh):
		self.dt = dt # Defined time in between interrupts
		self.batteryCapacityInC = batteryCapacityInAh*3600


	def estimate_start_SOC(self, voltageReading, testConstant): # ((JUST A TESTING FUNCTION - NOT DONE))
		self.SOC = voltageReading * testConstant 
		return self.SOC


	def esitmate_continuous_SOC(self, currentReading):
		self.SOC = self.SOC + currentReading * self.dt / self.batteryCapacityInC
		return self.SOC

# --------------- TEST ------------------
SOCtest = SOC(1, 13.889) # dt = 1 sekund, capacitet = 13.889 Ah = ~50000 Couloumb 
print(SOCtest.estimate_start_SOC(50,0.01)) # Voltage = 50V, factor = 0.01 -- start SOC = 0.5
print(SOCtest.esitmate_continuous_SOC(50000/2)) # Current = 25000A for 1 second = 25000 couloumbs (Final SOC should be 1!)
