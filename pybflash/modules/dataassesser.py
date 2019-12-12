from pybflash.libs.constants import *

class DataAssesser:
	"""docstring for DataAssesser"""
	def __init__(self, sensor_type):
		self.sensor_type = sensor_type

	def is_reading_ok(self, sensor_value):
		if self.sensor_type == 0:
			if sensor_value < MIN_TEMP_SENSOR or sensor_value > MAX_TEMP_SENSOR:
				return False
			else:
				return True
		elif self.sensor_type == 1:
			if sensor_value < MIN_CURRENT_SENSOR or sensor_value > MAX_CURRENT_SENSOR:
				return False
			else:
				return True
		elif self.sensor_type == 2:
			if sensor_value < MIN_VOLT_SENSOR or sensor_value > MAX_VOLT_SENSOR:
				return False
			else:
				return True
		else:
			print("No sensor type given")
		
	def is_soc_ok(self, soc_value):
		if soc_value < SOC_LOW_THRESHOLD:
			return False
		else:
			return True
#Has been tested and approved 08.12.19 by anders 'earsnot' rasmussen