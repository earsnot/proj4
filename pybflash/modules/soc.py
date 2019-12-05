class SOC:
	"""Docstring for soc - Handles estimation of SOC based on start voltage and couloumb counting (current integration)
	Input: dt (time in between interrupts), batteryCapacityInAh"""
	soc = 0

	def __init__(self, dt, battery_capacity_ah):
		self.dt = dt # Defined time in between interrupts
		self.battery_capacity_in_c = battery_capacity_ah*3600 # 1Ah = 3600 Coulombs


	def estimate_start_soc(self, voltage_reading, test_constant): # ((JUST A TESTING FUNCTION - NOT DONE))
		self.soc = voltage_reading * test_constant # Er soc på grafen fra 0-1 skal der ganges med 100 her.
		return self.soc


	def esitmate_continuous_soc(self, current_reading):
		self.soc = self.soc + (current_reading * self.dt * 100) / self.battery_capacity_in_c # *100 fordi procent
		return self.soc
