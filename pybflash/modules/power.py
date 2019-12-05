from libs.constants import *

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
		"""Docstring for calc_max_dis_power() - Calculates the maximum discharging power of the battery for a maximum
		10 second power draw"""
		minPower = self.minBatteryVoltage * (OCV - self.minBatteryVoltage) / self.dischargeResistance
		return minPower
