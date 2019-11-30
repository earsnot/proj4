# dump init stuff here
from pyb import Pin, ADC
import drivemodes
import libs.constants

def init():
    # initialising ADC
    voltage_adc = ADC(Pin(ADC_VOLT_PIN))
    current_adc = ADC(Pin(ADC_CURRENT_PIN))
    temperature_adc = ADC(Pin(ADC_TEMP_PIN))

    # ----------- Module instantiations
    # initialising modes
    eco = Mode(ECO)
    normal = Mode(NORMAL)
    sport = Mode(SPORT)

    # initialising DataAverager class
    avg_voltage = avg_data(AVG_WINDOW_SIZE)
    avg_current = avg_data(AVG_WINDOW_SIZE)
    avg_temp = avg_data(AVG_WINDOW_SIZE)

    # initialising Power class
    power = Power(MIN_BATTERY_VOLTAGE, R_DIS_DT_10S)

    # initialising SOC class
    soc = SOC(INTERRUPT_TIME, BATTERY_CAPACITY)

    # initialising ADCConvertor class
    adc_conv = ADCConvertor(ADC_VOLTAGE, ADC_BIT_SETTING)

    # initialising Scaler class
    volt_div_scaler = Scaler(VOLT_DIV_SCALE)



class LinearFunc:
	"""docstring for VoltageSensor - Input value and scale factor (fraction)"""
	def __init__(self, input_value, slope, intercept):
		self.input_value = input_value # expected input value
		self.slope = slope # slope coefficient
		self.intercept = intercept # interception point with y-axis

	def func_value(self):
		return self.slope*self.input_value+self.intercept # calculates value based on linear regression



print(eco)