
# -------- Constants for TEST
VOLTAGE_SENSOR_ID = 0  # Disse bliver defineret i constants
CURRENT_SENSOR_ID = 1
TEMP_SENSOR_ID = 2

ADC_VOLTAGE = 3.3  # [Volts]
ADC_BIT_SETTING = 10  # Denne setting er ikke officiel

# ------- Values for test
	voltage_sensor_bit_reading = 1<<9
	current_sensor_bit_reading = 1<<9
	temp_sensor_bit_reading = 1<<9

class MeasurementHandler:
	# Class variables
	voltage_avg = 0
	current_avg = 0
	temp_avg = 0


	def read_measurements(self):
		# VOLTAGE: Read, convert, and average voltage reading
		voltage_reading = voltage_adc.read() #
		voltage_converted = adc_conv.bit2voltage(voltage_reading)
		voltage_scaled = volt_div_scaler.scale(voltage_converted)
		voltage_averaged = avg_voltage.avg_data(voltage_scaled)

		current_reading = current_adc.read() #
		current_converted = adc_conv.bit2voltage(current_reading)
		current_scaled = cur_div_scaler.scale(current_converted)
		current_averaged = avg_voltage.avg_data(voltage_scaled)


		# CURRENT: Read, convert, and average voltage reading
		current_address = current_adc.getAddress(CURRENT_SENSOR_ID) # Comment: Hvad navn instancierer vi ADCAddressHandler som?
		# current_reading = getMeasurements(current_address) # Pseudo code
		current_reading = adc_convertor.bit2voltage(current_sensor_bit_reading)
		current_avg = DataAverager.average_data(current_reading) # Comment: Hvad navn instancierer vi average_data for Voltage som?


		# TEMPERATURE: Read, convert, and average voltage reading
		temp_address = ADCAddressHandler.getAddress(self.tempSensorID) # Comment: Hvad navn instancierer vi ADCAddressHandler som?
		# temp_reading = getMeasurements(temp_address) # Pseudo code
		temp_reading = adc_convertor.bit2voltage(temp_sensor_bit_reading)
		temp_avg = DataAverager.average_data(temp_reading) # Comment: Hvad navn instancierer vi average_data for Voltage som?



	def get_avg_voltage(self):
		return self.voltage_avg

	def get_avg_current(self):
		return self.current_avg

	def get_avg_temp(self):
		return self.temp_avg

# -------- Instanciations:

# ADCConvertor:
adc_convertor = ADCConvertor(ADC_VOLTAGE, ADC_BIT_SETTING) # instanciering af voltage adc konvertering

# ADCAdressHandler:
adc_address_voltage = ADCAdressHandler.getAddress(VOLTAGE_SENSOR_ID) # Comment: Hvad navn instancierer vi ADCAddressHandler som?
adc_address_current = ADCAdressHandler.getAddress(CURRENT_SENSOR_ID) # Comment: Hvad navn instancierer vi ADCAddressHandler som?
adc_address_temp = ADCAdressHandler.getAddress(TEMP_SENSOR_ID) # Comment: Hvad navn instancierer vi ADCAddressHandler som?

# DataAverager:

