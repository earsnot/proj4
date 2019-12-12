# dump init stuff here
from pybflash.libs.constants import *
from pybflash.modules.dataaverager import *
from pybflash.modules.power import *
from pybflash.modules.sensors import *
from pybflash.modules.soc import *


# ----------- Module instantiations
# initialising DataAverager class
avg_voltage = DataAverager(AVG_WINDOW_SIZE)
avg_current = DataAverager(AVG_WINDOW_SIZE)
avg_temp = DataAverager(AVG_WINDOW_SIZE)

# initialising Power class
power = Power(MIN_BATTERY_VOLTAGE, R_DIS_DT_10S)

# initialising ADCConvertor class
adc_conv = ADCConvertor(ADC_VOLTAGE, ADC_BIT_SETTING)

# initialising Scaler class
volt_div_scaler = Scaler(VOLT_DIV_SCALE)

# initialising LinearFunc class
current_func = LinearFunc(HALL_SEN_SLOPE, HALL_SEN_INTERCEPT)  # Hvad er slope og intercept af Hall Sensoren?
temp_func = LinearFunc(TEMP_SLOPE, TEMP_INTERCEPT)  # Hvad er slope og intercept af temperatursensoren?

# initialising SOC and OCV
soc_inst = SOCOCV(INTERRUPT_TIME, BATTERY_CAPACITY, SOC_SLOPE1, SOC_SLOPE2, SOC_SLOPE3, SOC_SLOPE4, SOC_INTERCEPT1, SOC_INTERCEPT2, SOC_INTERCEPT3, SOC_INTERCEPT4)
ocv_inst = SOCOCV(INTERRUPT_TIME, BATTERY_CAPACITY, OCV_SLOPE1, OCV_SLOPE2, OCV_SLOPE3, OCV_SLOPE4, OCV_INTERCEPT1, OCV_INTERCEPT2, OCV_INTERCEPT3, OCV_INTERCEPT4)

# initialising MeasurementHandler
#measurement_handler = MeasurementHandler()