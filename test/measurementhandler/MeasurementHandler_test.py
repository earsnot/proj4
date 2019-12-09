from init import *
from pybflash.libs.constants import *

test_volt_avg = DataAverager(30)
test_current_avg = DataAverager(30)
test_temp_avg = DataAverager(30)

class MeasurementHandler:

	def __init__(self):
		self.voltage_avg = 0
		self.current_avg = 0
		self.temp_avg = 0
		self.max_dis_pwr = 0
		self.power = 0
		self.ocv = 0
		self.soc = 0

	def read_measurements(self, test_volt_reading, test_curr_reading, test_temp_reading):
		# VOLTAGE: Read, convert, and average voltage reading

		voltage_avg_test = 0
		voltage_reading = test_volt_reading
		voltage_converted = adc_conv.bit2voltage(voltage_reading) # Convert bit-value to voltage
		voltage_scaled = volt_div_scaler.scale(voltage_converted) # Scale voltage to original value, before voltage div
		self.voltage_avg = avg_voltage.avg_data(voltage_scaled) # Average voltage reading

		# CURRENT: Read, convert, and average voltage reading
		current_reading = test_curr_reading
		current_converted = adc_conv.bit2voltage(current_reading) # Convert bit-value to voltage
		current_scaled = current_func.func_value(current_converted) # Scale voltage to original value with function
		self.current_avg = avg_current.avg_data(current_scaled) # Average current reading

		# TEMPERATURE: Read, convert, and average voltage reading
		temp_reading = test_temp_reading
		temp_converted = adc_conv.bit2voltage(temp_reading)  # Convert bit-value to voltage
		temp_scaled = temp_func.func_value(temp_converted)  # Scale voltage to original value with function
		self.temp_avg = avg_temp.avg_data(temp_scaled)  # Average current reading

	def calculate_parameters(self):
		self.soc = soc_inst.estimate_continuous_soc(self.current_avg)
		self.ocv = ocv_inst.estimate_ocv()

		self.power = power.calc_power(self.current_avg, self.voltage_avg)
		self.max_dis_pwr = power.calc_max_dis_power(self.ocv)


	def get_avg_voltage(self):
		return self.voltage_avg

	def get_avg_current(self):
		return self.current_avg

	def get_avg_temp(self):
		return self.temp_avg


# --------- Test bench:
measurement_test = MeasurementHandler()

measurement_test.read_measurements(3500,3000,3500)
measurement_test.read_measurements(3500,3000,3500)
measurement_test.read_measurements(3500,3000,3500)
measurement_test.read_measurements(3500,3000,3500)

print(measurement_test.voltage_avg)
print(measurement_test.current_avg)
print(measurement_test.temp_avg)

measurement_test.calculate_parameters()


print(measurement_test.soc)
print(measurement_test.ocv)
print(measurement_test.power)
print(measurement_test.max_dis_pwr)