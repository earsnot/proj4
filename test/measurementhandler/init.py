# dump init stuff here
from libs.constants import *
#from pybflash.modules.dataaverager import *
from pybflash.modules.power import *
from pybflash.modules.sensors import *
from pybflash.modules.soc import *


# ----------- Module instantiations
# initialising DataAverager class
#avg_voltage = DataAverager(30)
#avg_current = DataAverager(30)
#avg_temp = DataAverager(30)

# initialising Power class
power = Power(MIN_BATTERY_VOLTAGE, R_DIS_DT_10S)

# initialising SOC class
soc = SOC(INTERRUPT_TIME, BATTERY_CAPACITY)

# initialising ADCConvertor class
adc_conv = ADCConvertor(3.3, 12)

# initialising Scaler class
volt_div_scaler = Scaler(14)

# initialising LinearFunc class
current_func = LinearFunc(2, 3)  # Hvad er slope og intercept af Hall Sensoren?
temp_func = LinearFunc(4, 5)  # Hvad er slope og intercept af temperatursensoren?