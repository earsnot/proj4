class ADCConvertor:
	"""docstring for VoltageSensor - Input value and scale factor (fraction)"""
	def __init__(self, ADCvoltage, bitreading, bitconfig):
		self.ADCvoltage = ADCvoltage # voltage range from ADC
		self.bitreading = bitreading # the measured input voltage in bit value
		self.bitconfig = bitconfig # configurated bit-setting

	def bit2voltage(self):
		return self.ADCvoltage*self.bitreading/(1<<self.bitconfig) # calculates bit to voltage (sensor)

class Scaler:
	"""docstring for VoltageSensor - Input value and scale factor (fraction)"""
	def __init__(self, input_value, factor):
		self.input_value = input_value # input value for scaling
		self.factor = factor # expected input is a fraction (voltage divider)

	def scale(self):
		return self.factor*self.input_value # scales input value with given factor

class LinearFunc:
	"""docstring for VoltageSensor - Input value and scale factor (fraction)"""
	def __init__(self, input_value, slope, intercept):
		self.input_value = input_value # expected input value
		self.slope = slope # slope coefficient
		self.intercept = intercept # interception point with y-axis

	def func_value(self):
		return self.slope*self.input_value+self.intercept # calculates value based on linear regression