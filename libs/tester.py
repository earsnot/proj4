from constants import *

class DataAssesser:
	"""docstring for DataAssesser"""
	tester = 2

	def check_sensor_readings(sensorType, sensorValue):
		if sensorType == 0:
			if sensorValue < MIN_TEMP_SENSOR or sensorValue > MAX_TEMP_SENSOR:
				return 1
		elif sensorType == 1:
			if sensorValue < MIN_CURRENT_SENSOR or sensorValue > MAX_CURRENT_SENSOR:
				return 1
		elif sensorType == 2:
			if sensorValue < MIN_VOLT_SENSOR or sensorValue > MAX_VOLT_SENSOR:
				return 1
		else:
			return 0
		
	def check_if_SOC_too_low(SOCValue):
		if SOCValue < SOC_LOW_THRESHOLD:
			return 1
		else:
			return 0
	

dataassesser = DataAssesser
voltage_check = dataassesser.check_sensor_readings(0, 30)
current_sensor_check = dataassesser.check_sensor_readings(1,30)
