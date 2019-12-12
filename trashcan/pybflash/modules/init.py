# dump init stuff here
from pyb import *
from libs.constants import *
from modules.drivemodes import *
from modules.dataaverager import *
from modules.dataassesser import *
from modules.power import *
from modules.sensors import *
from modules.soc import *


# initialising ADC
voltage_adc = ADC(Pin(ADC_VOLT_PIN))
current_adc = ADC(Pin(ADC_CURRENT_PIN))
temperature_adc = ADC(Pin(ADC_TEMP_PIN))

# ----------- Module instantiations
# initialising modes
eco = Mode(ECO_PIN)
normal = Mode(NORMAL_PIN)
sport = Mode(SPORT_PIN)

# initialising DataAverager class
avg_voltage = DataAverager(AVG_WINDOW_SIZE)
avg_current = DataAverager(AVG_WINDOW_SIZE)
avg_temp = DataAverager(AVG_WINDOW_SIZE)

# initialising Power class
power = Power(MIN_BATTERY_VOLTAGE, R_DIS_DT_10S)

# initialising SOC class
soc = SOC(INTERRUPT_TIME, BATTERY_CAPACITY)

# initialising ADCConvertor class
adc_conv = ADCConvertor(ADC_VOLTAGE, ADC_BIT_SETTING)

# initialising Scaler class
volt_div_scaler = Scaler(VOLT_DIV_SCALE)

# initialising LinearFunc class
current_func = LinearFunc(HALL_SEN_SLOPE, HALL_SEN_INTERCEPT)  # Hvad er slope og intercept af Hall Sensoren?
temp_func = LinearFunc(TEMP_SLOPE, TEMP_INTERCEPT)  # Hvad er slope og intercept af temperatursensoren?

#Has been tested and approved 08.12.19 by anders 'earsnot' rasmussen
