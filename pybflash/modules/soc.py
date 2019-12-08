# Test includes:
from libs.constants import *

# Test voltage limits:
V1 = 40
V2 = 43
V3 = 45
V4 = 49
V5 = 54

class SOCOCV:
	"""Docstring for soc - Handles estimation of SOC based on start voltage and couloumb counting (current integration)
	Input: dt (time in between interrupts), batteryCapacityInAh"""
	soc = 0

	def __init__(self, dt, battery_capacity_ah, slope1, slope2, slope3, slope4, intercept1, intercept2, intercept3, intercept4):
		self.dt = dt # Defined time in between interrupts
		self.batteryCapacityInC = battery_capacity_ah*3600 # 1Ah = 3600 Coulombs
		self.slope1 = slope1
		self.slope2 = slope2
		self.slope3 = slope3
		self.slope4 = slope4
		self.intercept1 = intercept1
		self.intercept2 = intercept2
		self.intercept3 = intercept3
		self.intercept4 = intercept4


	def estimate_ocv(self):
		if 0 < self.soc < 9.9625:
			ocv = self.soc * self.slope1 + self.intercept1
		elif 9.9625 <= self.soc < 30.0875:
			ocv = self.soc * self.slope2 + self.intercept2
		elif 30.0875 <= self.soc < 75:
			ocv = self.soc * self.slope3 + self.intercept3
		elif 75 <= self.soc < 100:
			ocv = self.soc * self.slope4 + self.intercept4
		else:
			pass

		return ocv

	def estimate_start_SOC(self, voltageReading): # ((JUST A TESTING FUNCTION - NOT DONE))

		if V1 < voltageReading < V2:
			self.soc = voltageReading * self.slope1 + self.intercept1
		elif V2 <= voltageReading < v3:
			self.soc = voltageReading * self.slope2 + self.intercept2
		elif V3 <= voltageReading < v4:
			self.soc = voltageReading * self.slope3 + self.intercept3
		elif V4 <= voltageReading < V5:
			self.soc = voltageReading * self.slope4 + self.intercept4
		else:
			pass


soc = SOCOCV(0.1, 18, 1,2,3,4,5,6,7,8)
ocv = SOCOCV(0.1, 18, 1,2,3,4,5,6,7,8)

soc.estimate_start_SOC()