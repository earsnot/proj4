
# Constants for TEST
VOLTAGE_SENSOR_ID = 0  # Disse bliver defineret i constants
CURRENT_SENSOR_ID = 1
TEMP_SENSOR_ID = 2

ADC_VOLTAGE = 3.3  # [Volts]

ADC_BIT_SETTING = 10  # Denne setting er ikke officiel


# Values for test
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
		voltage_address = ADCAddressHandler.getAddress(self.voltageSensorID) # Comment: Hvad navn instancierer vi ADCAddressHandler som?
		voltageReading = getMeasurements(voltage_address) # Pseudo code
		ADCConvertor.bit2voltage(voltage_sensor_bit_reading)

		# Indsæt bit2voltage (hvad end Troels har kaldt den)
		voltage_avg = DataAverager.average_data(voltageReading) # Comment: Hvad navn instancierer vi average_data for Voltage som?

		# VOLTAGE: Read, convert, and average voltage reading
		currentAddress = ADCAddressHandler.getAddress(self.currentSensorID) # Comment: Hvad navn instancierer vi ADCAddressHandler som?
		currentReading = getMeasurements(currentAddress) # Pseudo code


		current_avg = DataAverager.average_data(voltageReading) # Comment: Hvad navn instancierer vi average_data for Voltage som?

		# VOLTAGE: Read, convert, and average voltage reading
		tempAddress = ADCAddressHandler.getAddress(self.tempSensorID) # Comment: Hvad navn instancierer vi ADCAddressHandler som?
		tempReading = getMeasurements(tempAddress) # Pseudo code
		tempAvg = DataAverager.average_data(voltageReading) # Comment: Hvad navn instancierer vi average_data for Voltage som?



	def get_avg_voltage(self):
		return self.voltageAvg

	def get_avg_current(self):
		return self.currentAvg

	def get_avg_temp(self):
		return self.tempAvg

# Instanciations:

# ADCConvertor:
voltage_adc = ADCConvertor(ADC_VOLTAGE, ADC_BIT_SETTING) # instanciering af voltage adc konvertering
current_adc = ADCConvertor(ADC_VOLTAGE, ADC_BIT_SETTING) # instanciering af voltage adc konvertering
temp_adc = ADCConvertor(ADC_VOLTAGE, ADC_BIT_SETTING) # instanciering af voltage adc konvertering

# ADCAdressHandler:
adc_address_voltage = ADCAdressHandler.getAddress(VOLTAGE_SENSOR_ID) # Comment: Hvad navn instancierer vi ADCAddressHandler som?
adc_address_current = ADCAdressHandler.getAddress(CURRENT_SENSOR_ID) # Comment: Hvad navn instancierer vi ADCAddressHandler som?
adc_address_temp = ADCAdressHandler.getAddress(TEMP_SENSOR_ID) # Comment: Hvad navn instancierer vi ADCAddressHandler som?

