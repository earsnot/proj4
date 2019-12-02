class Alarms:
	"""docstring for Alarms"""
		
	def alarm_SOC(flag):
		if flag == 1:
			return "SOC below threshold"
		
	def alarm_sensors(type, flag):
		if flag == 1:
			String = " sensor out of bounce"
			if type == 0:
				return "Temp"+String
			elif type == 1:
				return "Current"+String
			elif type == 2:
				return "Voltage"+String


A = Alarms
print(A.alarm_SOC(0))