from constants import *

class DataAssesser:
	"""docstring for DataAssesser"""
	def __init__(self, sensorValue , sensorType):
		self.sensorValue = sensorValue
		self.sensorType = sensorType

	def check_sensor_readings(self):
		if self.sensorType == 0:
			if self.sensorValue < MIN_TEMP_SENSOR or self.sensorValue > MAX_TEMP_SENSOR:
				return 0
		elif self.sensorType == 1:
			if self.sensorValue < MIN_TEMP_SENSOR or self.sensorValue > MAX_CURENT_SENSOR:
				return 1
		elif self.sensorType == 2:
			if self.sensorValue < MIN_VOLT_SENSOR or self.sensorValue > MAX_VOLT_SENSOR:
				return 2
		

A = DataAssesser(34,2)
print(A.check_sensor_readings())