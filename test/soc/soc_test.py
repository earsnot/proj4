from libs.constants import *

class SOCOCV:
	"""Docstring for SOCOCV - SOC / OCV calculation - Handles estimation of soc based on start voltage and couloumb
	counting (current integration). Handles calculation of ocv based on soc.
	Input: dt (time in between interrupts), battery_capacity_ah, slopes and intercepts of functions"""
	soc = 0

	def __init__(self, dt, battery_capacity_ah, slope1, slope2, slope3, slope4, intercept1, intercept2, intercept3, intercept4):
		self.dt = dt # Defined time in between interrupts
		self.battery_capacity_in_c = battery_capacity_ah * 3600 # 1Ah = 3600 Coulombs
		self.slope1 = slope1
		self.slope2 = slope2
		self.slope3 = slope3
		self.slope4 = slope4
		self.intercept1 = intercept1
		self.intercept2 = intercept2
		self.intercept3 = intercept3
		self.intercept4 = intercept4


	def estimate_ocv(self, test_soc):
		if 0 <= test_soc < 9.963:
			ocv = test_soc * self.slope1 + self.intercept1
		elif 9.963 <= test_soc < 30.088:
			ocv = test_soc * self.slope2 + self.intercept2
		elif 30.088 <= test_soc < 75:
			ocv = test_soc * self.slope3 + self.intercept3
		elif 75 <= test_soc <= 100:
			ocv = test_soc * self.slope4 + self.intercept4
		else:
			ocv = -1
		return ocv

	def estimate_start_soc(self, voltage_reading):
		if 46.5505 <= voltage_reading < 47.384:
			self.soc = voltage_reading * self.slope1 + self.intercept1
			print("1")
		elif 47.384 <= voltage_reading < 48.667:
			self.soc = voltage_reading * self.slope2 + self.intercept2
			print("2")
		elif 48.667 <= voltage_reading < 50.98:
			self.soc = voltage_reading * self.slope3 + self.intercept3
			print("3")
		elif 50.980 <= voltage_reading <= 52.357:
			self.soc = voltage_reading * self.slope4 + self.intercept4
			print("4")
		else:
			self.soc = -1
		return self.soc

	def estimate_continuous_soc(self, current_reading):
		self.soc = self.soc + (current_reading * self.dt * 100) / self.battery_capacity_in_c # *100 fordi procent
		return self.soc


soc_inst = SOCOCV(INTERRUPT_TIME, BATTERY_CAPACITY, SOC_SLOPE1, SOC_SLOPE2, SOC_SLOPE3, SOC_SLOPE4, SOC_INTERCEPT1, SOC_INTERCEPT2, SOC_INTERCEPT3, SOC_INTERCEPT4)
ocv_inst = SOCOCV(INTERRUPT_TIME, BATTERY_CAPACITY, OCV_SLOPE1, OCV_SLOPE2, OCV_SLOPE3, OCV_SLOPE4, OCV_INTERCEPT1, OCV_INTERCEPT2, OCV_INTERCEPT3, OCV_INTERCEPT4)
soc_inst.estimate_start_soc(48)