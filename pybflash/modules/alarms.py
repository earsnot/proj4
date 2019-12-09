class Alarms:
	"""docstring for Alarms"""
	@staticmethod
	def alarm_soc(flag):
		if flag == 1:
			return "SOC below threshold"
	@staticmethod
	def alarm_sensors(type, flag):
		if flag == 1:
			String = "sensor out of bounds"
			if type == 0:
				return "Temp"+String
			elif type == 1:
				return "Current"+String
			elif type == 2:
				return "Voltage"+String
			else:
				pass