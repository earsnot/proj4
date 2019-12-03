# Test constants (These are loacted in the 'constants' module)
MIN_BATTERY_VOLTAGE = 42 # Volts
MAX_BATTERY_VOLTAGE = 52 # Volts
R_DIS_DT_10S = 0.28 # [Ohms] (3.7V / 13.2A) - 10 second voltage drop test - From ballpark test. Resistance calculated
					# from voltage drop over 10 seconds divided by current draw.


class Power:
	"""Docstring for Power class - Handles calculation of power and minimum allowed power draw
	Input: minBatteryVoltage, dischargeResistance."""
	def __init__(self, minBatteryVoltage, dischargeResistance):
		self.minBatteryVoltage = minBatteryVoltage
		self.dischargeResistance = dischargeResistance

	def calc_power(self, currentReading, voltageReading):
		power = currentReading * voltageReading # 
		return power

	def calc_max_dis_power(self, OCV): # OCV: Should be calculated from an external function through the OCV/SOC curve.
		"""Docstring for calc_max_dis_power() - Calculates the maximum discharging power of the battery for a maximum 10 second power draw"""
		minPower = self.minBatteryVoltage * (OCV - self.minBatteryVoltage) / self.dischargeResistance
		return minPower

## ----------- Test --------------
#Powertest = Power(MIN_BATTERY_VOLTAGE, R_DIS_DT_10S)
#print(Powertest.calc_max_dis_power(42.5))
#print(Powertest.calc_power(10, 10))
