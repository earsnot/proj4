from init import *


# Test bench variables
test_volt_bit_reading = 3500.5
test_curr_bit_reading = 2000.5
test_temp_bit_reading = 1500.5


# DataAverager just for testing:
class DataAverager:
	"""docstring for DataAverager - Handles moving averaging of data over a defined windows size.
	Input: averageSize (averaging window size)."""

	def __init__(self, average_size):
		self.average_size = average_size  # The amount of data points to average over
		self.measurements = [] # Define list to average over
	def avg_data(self, measurement):
		sum_of = 0  # container for the average sum value

		if len(
				self.measurements) >= self.average_size:  # If there are "average_size" amount of measurements in the list,
													      # delete the oldest measurement
			self.measurements.pop()

		self.measurements.insert(0, measurement)  # Insert the newest measurement at the first index of the list

		for i in self.measurements:  # Summarize every index of the measurement list into one variable: sum
			sum_of += i

		return sum_of / len(self.measurements)  # Divide the sum with amount of measurements

test_volt_avg = DataAverager(30)
test_current_avg = DataAverager(30)
test_temp_avg = DataAverager(30)

class MeasurementHandler:

	def __init__(self):
		self.voltage_avg = 0
		self.current_avg = 0
		self.temp_avg = 0


	def read_measurements(self, test_volt_reading, test_curr_reading, test_temp_reading):
		# VOLTAGE: Read, convert, and average voltage reading

		voltage_avg_test = 0
		voltage_reading = test_volt_reading
		voltage_converted = adc_conv.bit2voltage(voltage_reading) # Convert bit-value to voltage
		voltage_scaled = volt_div_scaler.scale(voltage_converted) # Scale voltage to original value, before voltage div
		self.voltage_avg = test_volt_avg.avg_data(voltage_scaled) # Average voltage reading

		# CURRENT: Read, convert, and average voltage reading
		current_reading = test_curr_reading
		current_converted = adc_conv.bit2voltage(current_reading) # Convert bit-value to voltage
		current_scaled = current_func.func_value(current_converted) # Scale voltage to original value with function
		self.current_avg = test_current_avg.avg_data(current_scaled) # Average current reading

		# TEMPERATURE: Read, convert, and average voltage reading
		temp_reading = test_temp_reading
		temp_converted = adc_conv.bit2voltage(temp_reading)  # Convert bit-value to voltage
		temp_scaled = temp_func.func_value(temp_converted)  # Scale voltage to original value with function
		self.temp_avg = test_temp_avg.avg_data(temp_scaled)  # Average current reading



	def get_avg_voltage(self):
		return self.voltage_avg

	def get_avg_current(self):
		return self.current_avg

	def get_avg_temp(self):
		return self.temp_avg

measurement_test = MeasurementHandler()



measurement_test.read_measurements(1000, 2000, 3000)
print(measurement_test.get_avg_voltage())
print(measurement_test.get_avg_current())
print(measurement_test.get_avg_temp())

measurement_test.read_measurements(1000, 2500, 3500)
print(measurement_test.get_avg_voltage())
print(measurement_test.get_avg_current())
print(measurement_test.get_avg_temp())

measurement_test.read_measurements(1000, 2750, 3750)
print(measurement_test.get_avg_voltage())
print(measurement_test.get_avg_current())
print(measurement_test.get_avg_temp())

measurement_test.read_measurements(3512, 2315, 221)
print(measurement_test.get_avg_voltage())
print(measurement_test.get_avg_current())
print(measurement_test.get_avg_temp())

measurement_test.read_measurements(242, 123, 4212)
print(measurement_test.get_avg_voltage())
print(measurement_test.get_avg_current())
print(measurement_test.get_avg_temp())