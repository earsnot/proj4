class DataAverager:
	"""docstring for DataAverager"""
	measurements = [] # Make list

	def __init__(self, averageSize):
		self.averageSize = averageSize # The amount of data points to average over

	def average(self, measurement):
		sum = 0 # container for the average 

		if len(self.measurements) >= self.averageSize:
			self.measurements.pop()

		self.measurements.insert(0, measurement)

		for i in self.measurements:
			sum += i

		return sum/len(self.measurements) # Devide the sum with amount of measurements


# --------------- TEST -----------------
molle = DataAverager(30)
for i in range(31): # range(10) = a list from 0 to 9 (lengeth of 10)
	print(i)
	print(molle.average(i))

