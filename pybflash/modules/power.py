class Power:
	"""Docstring for Power class - Handles calculation of power and maximum allowed power draw for a 10s period
	Input: min_battery_voltage, discharge_resistance."""
	def __init__(self, min_battery_voltage, discharge_resistance):
		self.min_battery_voltage = min_battery_voltage
		self.discharge_resistance = discharge_resistance

	def calc_power(self, current_reading, voltage_reading):
		power = current_reading * voltage_reading
		return power

	def calc_max_dis_power(self, ocv): # ocv: Should be calculated from an external function through the ocv/SOC curve.
		"""Docstring for calc_max_dis_power() - Calculates the maximum discharging power of the battery for a maximum
		10 second power draw"""
		minPower = self.min_battery_voltage * (ocv - self.min_battery_voltage) / self.discharge_resistance
		return minPower

#Has been tested and approved 09.12.19 by anders 'earsnot' rasmussen
