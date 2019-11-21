class ADCConvertor:
	INPUT_VOLTAGE = 3.3
	"""docstring for VoltageSensor - Input value and scale factor (fraction)"""
	def __init__(self, bitreading, bitconfig):
		self.bitreading = bitreading # the measured input voltage
		self.bitconfig = bitconfig # configurated bit-setting

	def bit2voltage(self):
		return self.INPUT_VOLTAGE*self.bitreading/pow(2,self.bitconfig)


class VoltageSensor:
	"""docstring for VoltageSensor - Input value and scale factor (fraction)"""
	def __init__(self, factor):
		self.factor = factor # expected input is a fraction (voltage divider)

	def voltage_divider(self):
		return self.INPUT_VOLTAGE*self.bit2voltage()/self.factor


class VoltageSensor_TESTER:
	"""docstring for VoltageSensor - Input value and scale factor (fraction)"""
	def __init__(self, voltage, factor):
		self.voltage = voltage
		self.factor = factor # expected input is a fraction (voltage divider)

	def voltage_divider(self):
		return self.voltage/self.factor


class CurrentSensor:
	SLOPE = 10.674
	INTERCEPT = -45.291
	"""docstring for VoltageSensor - Input value and scale factor (fraction)"""
	def __init__(self, bitreading, factor, bit):
		self.bitreading = bitreading # the measured input voltage
		self.factor = factor # expected input is a fraction (voltage divider)
		self.bit = bit # configurated bit-setting

	def bit2voltage(self):
		return self.bitreading/pow(2,self.bit)

	def voltageDivider(self):
		return self.INPUT_VOLTAGE*self.bit2voltage()/self.factor

V1 = VoltageSensor_TESTER(5, 0.1)
print(V1.voltage_divider())

