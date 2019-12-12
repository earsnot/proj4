from libs.constants import *

class DataAssesser:
	"""docstring for DataAssesser"""
	def __init__(self, sensor_type):
		self.sensor_type = sensor_type

	def check_sensor_readings(self, sensor_value):
		if self.sensor_type == 0:
			if sensor_value < MIN_TEMP_SENSOR or sensor_value > MAX_TEMP_SENSOR:
				return 1
		elif self.sensor_type == 1:
			if sensor_value < MIN_CURRENT_SENSOR or sensor_value > MAX_CURRENT_SENSOR:
				return 1
		elif self.sensor_type == 2:
			if sensor_value < MIN_VOLT_SENSOR or sensor_value > MAX_VOLT_SENSOR:
				return 1
		else:
			return 0
		
	def check_if_soc_too_low(self, soc_value):
		if soc_value < SOC_LOW_THRESHOLD:
			return 1
		else:
			return 0
