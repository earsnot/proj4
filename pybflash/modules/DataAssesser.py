class DataAssesser:
	"""docstring for DataAssesser"""
	def __init__(self, sensorType):
		self.sensorType = sensorType

	def check_sensor_readings(self, sensorValue):
		if self.sensorType == 0:
			if sensorValue < MIN_TEMP_SENSOR or sensorValue > MAX_TEMP_SENSOR:
				return 1
		elif self.sensorType == 1:
			if sensorValue < MIN_CURRENT_SENSOR or sensorValue > MAX_CURRENT_SENSOR:
				return 1
		elif self.sensorType == 2:
			if sensorValue < MIN_VOLT_SENSOR or sensorValue > MAX_VOLT_SENSOR:
				return 1
		else:
			return 0
		
	def check_if_SOC_too_low(self, SOCValue):
		if SOCValue < SOC_LOW_THRESHOLD:
			return 1
		else:
			return 0
