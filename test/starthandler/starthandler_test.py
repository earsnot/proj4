from init import *
from pybflash.modules.dataassesser import *
from pybflash.modules.alarms import *


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

	def get_power(self):
		return self.power

	def get_max_dis_pwr(self):
		return self.max_dis_pwr

	def get_soc(self):
		return self.soc


measurement_handler = MeasurementHandler()

volt_assessor = DataAssesser(TYPE_VOLT_SENSOR)
curr_assessor = DataAssesser(TYPE_CURRENT_SENSOR)
temp_assessor = DataAssesser(TYPE_TEMP_SENSOR)


class StartHandler:

	def __init__(self):
		self.avg_voltage = 0
		self.avg_current = 0
		self.avg_temp = 0
		self.power = 0
		self.max_dis_pwr = 0
		self.soc = 0


	def run_start(self):
		# Read measurements and calculate parameters
		measurement_handler.read_measurements(3600,2500,1100) # Bruger _test versionen for at kunne indsætte målinger

		# Get values
		self.avg_voltage = measurement_handler.get_avg_voltage()
		self.avg_current = measurement_handler.get_avg_current()
		self.avg_temp = measurement_handler.get_avg_temp()

		# Calculate start SOC
		self.soc = soc_inst.estimate_start_soc(self.avg_voltage)

		# Calculate parameters and get them
		measurement_handler.calculate_parameters()
		self.power = measurement_handler.get_power()
		self.max_dis_pwr = measurement_handler.get_max_dis_pwr()
		self.soc = measurement_handler.get_soc()


		# Check voltage readings
		alarm_flag_soc = DataAssesser.check_if_soc_too_low(self.soc)
		alarm_flag_volt = volt_assessor.check_sensor_readings(self.avg_voltage)
		alarm_flag_curr = curr_assessor.check_sensor_readings(self.avg_current)
		alarm_flag_temp = temp_assessor.check_sensor_readings(self.avg_temp)

		print("\r\nFlags are:")
		print(alarm_flag_soc)
		print(alarm_flag_volt)
		print(alarm_flag_curr)
		print(alarm_flag_temp)

		# Get alarm strings
		print("\r\nAlarm strings are:")
		alarm_string_soc = Alarms.alarm_soc(alarm_flag_soc)
		alarm_string_volt = Alarms.alarm_sensors(TYPE_VOLT_SENSOR,alarm_flag_temp)
		alarm_string_curr = Alarms.alarm_sensors(TYPE_CURRENT_SENSOR,alarm_flag_curr)
		alarm_string_temp = Alarms.alarm_sensors(TYPE_TEMP_SENSOR,alarm_flag_temp)

		# print alarm strings
		print(alarm_string_soc)
		print(alarm_string_volt)
		print(alarm_string_curr)
		print(alarm_string_temp)


start_handler_test = StartHandler()
start_handler_test.run_start()

print("\r\nMeasuremnets are are:")
print("voltage: ",start_handler_test.avg_voltage)
print("current: ",start_handler_test.avg_current)
print("tempreatue: ",start_handler_test.avg_temp)
print("\r\nCalcs are:")
print(start_handler_test.power)
print(start_handler_test.max_dis_pwr)
print(start_handler_test.soc)
