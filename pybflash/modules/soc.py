class SOCOCV:
	"""Docstring for SOC/OCV - Handles estimation of soc based on start voltage and couloumb counting
	(current integration)
	Input: dt (time in between interrupts), batteryCapacityInAh"""
	soc = 0

	def __init__(self, dt, battery_capacity_ah, slope1, slope2, slope3, slope4, intercept1, intercept2, intercept3, intercept4):
		self.dt = dt # Defined time in between interrupts
		self.batter_capacity_in_c = battery_capacity_ah*3600 # 1Ah = 3600 Coulombs
		self.slope1 = slope1
		self.slope2 = slope2
		self.slope3 = slope3
		self.slope4 = slope4
		self.intercept1 = intercept1
		self.intercept2 = intercept2
		self.intercept3 = intercept3
		self.intercept4 = intercept4


	def estimate_ocv(self): # Estimates ocv based on the soc. Depending on the soc different functions are used.
		if 0 <= self.soc < 9.9625:
			ocv = self.soc * self.slope1 + self.intercept1
		elif 9.9625 <= self.soc < 30.0875:
			ocv = self.soc * self.slope2 + self.intercept2
		elif 30.0875 <= self.soc < 75:
			ocv = self.soc * self.slope3 + self.intercept3
		elif 75 <= self.soc <= 100:
			ocv = self.soc * self.slope4 + self.intercept4
		else:
			ocv = -1 # If the soc is beyond the defined, return -1
		return ocv


	def estimate_start_soc(self, voltage_reading): # Estimates the soc based on the voltage reading. Different functions
# are used depending on the voltage reading.
		if 46.5505 <= voltage_reading < 47.384:
			self.soc = voltage_reading * self.slope1 + self.intercept1
		elif 47.384 <= voltage_reading < 48.667:
			self.soc = voltage_reading * self.slope2 + self.intercept2
		elif 48.667 <= voltage_reading < 50.98:
			self.soc = voltage_reading * self.slope3 + self.intercept3
		elif 50.980 <= voltage_reading <= 52.357:
			self.soc = voltage_reading * self.slope4 + self.intercept4
		else:
			self.soc = -1 # If the voltage reading is beyond the defined, return -1
		return self.soc

	def estimate_continuous_soc(self, current_reading):
		self.soc = self.soc + (current_reading * self.dt * 100) / self.batter_capacity_in_c # *100 fordi procent
		return self.soc