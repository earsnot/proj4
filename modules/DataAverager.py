class DataAverager:
	"""docstring for DataAverager - Handles moving averaging of data over a defined windows size.
	Input: averageSize (averaging window size)."""
	
	measurements = [] # Define list to average over

	def __init__(self, averageSize):
		self.averageSize = averageSize # The amount of data points to average over

	def average(self, measurement):
		sum = 0 # container for the average 

		if len(self.measurements) >= self.averageSize: # If there are "averageSize" amount of measurements in the list, delete the oldest measurement
			self.measurements.pop()

		self.measurements.insert(0, measurement) # Insert the newest measurement at the first index of the list

		for i in self.measurements: # Summarize every index of the measurement list into one variable, sum 
			sum += i

		return sum/len(self.measurements) # Divide the sum with amount of measurements


# --------------- TEST -----------------
#molle = DataAverager(30)
#for i in range(31): # range(10) = a list from 0 to 9 (lengeth of 10)
#	print(i)
#	print(molle.average(i))

