class SOC:
	"""docstring for SOC - Handles estimation of SOC based on start voltage and couloumb counting (current integration)
	Input = dt (1/interrupt frequency)"""
	SOC = 0
	def __init__(self, dt, totalCapacity):
		self.dt = dt # Defined time in between interrupts
		self.totalCapacity = totalCapacity # Define the total capacity of the battery in coulombs

	def estimate_start_SOC(self, voltageReading, testConstant):
		self.SOC = voltageReading * testConstant
		return self.SOC


	def esitmate_continuous_SOC(self, currentReading):
		self.SOC = self.SOC + currentReading * self.dt / self.totalCapacity
		return self.SOC

SOCtest = SOC(10, 50000)

print(SOCtest.estimate_start_SOC(50,0.01))

for i in range(100):
	print(SOCtest.esitmate_continuous_SOC(10))
