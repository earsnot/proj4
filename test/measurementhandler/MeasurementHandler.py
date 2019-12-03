class MeasurementHandler:
	# Class variables
	voltage_avg = 0
	current_avg = 0
	temp_avg = 0


	def read_measurements(self):
		# VOLTAGE: Read, convert, and average voltage reading
		voltage_reading = voltage_adc.read() # Read ADC bit value from PyBoard ADC
		voltage_converted = adc_conv.bit2voltage(voltage_reading) # Convert bit-value to voltage
		voltage_scaled = volt_div_scaler.scale(voltage_converted) # Scale voltage to original value, before voltage div
		self.voltage_avg = avg_voltage.avg_data(voltage_scaled) # Average voltage reading

		# CURRENT: Read, convert, and average voltage reading
		current_reading = current_adc.read() # Read ADC bit value from PyBoard ADC
		current_converted = adc_conv.bit2voltage(current_reading) # Convert bit-value to voltage
		current_scaled = current_func.func_value(current_converted) # Scale voltage to original value with function
		self.current_avg = avg_current.avg_data(current_scaled) # Average current reading

		# TEMPERATURE: Read, convert, and average voltage reading
		temp_reading = temp_adc.read()  # Read ADC bit value from PyBoard ADC
		temp_converted = adc_conv.bit2voltage(temp_reading)  # Convert bit-value to voltage
		temp_scaled = temp_func.func_value(temp_converted)  # Scale voltage to original value with function
		self.temp_avg = avg_temp.avg_data(temp_scaled)  # Average current reading


	def get_avg_voltage(self):
		return self.voltage_avg

	def get_avg_current(self):
		return self.current_avg

	def get_avg_temp(self):
		return self.temp_avg


