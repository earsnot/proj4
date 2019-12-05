from libs.constants import *

class DataAverager:
	"""docstring for DataAverager - Handles moving averaging of data over a defined windows size.
	Input: average_size (averaging window size)."""

	measurements = []  # Define list to average over

	def __init__(self, average_size):
		self.average_size = average_size  # The amount of data points to average over

	def avg_data(self, measurement):
		sum_of = 0  # container for the average sum value

		# If there are "average_size" amount of measurements in the list,
		if len(self.measurements) >= self.average_size:
														# delete the oldest measurement
			self.measurements.pop()

		# Insert the newest measurement at the first index of the list
		self.measurements.insert(0, measurement)

		for i in self.measurements:  # Summarize every index of the measurement list into one variable: sum
			sum_of += i

		# Divide the sum with amount of measurements
		return sum_of / len(self.measurements)
