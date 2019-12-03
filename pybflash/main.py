# main.py -- put your code here!
from modules.DataAverager import *
from modules.DataAssesser import *
from modules.Power import *
#from modules.init import *
from modules.SOC import *
from modules.drivemodes import *
from modules.sensors import *
from libs.constants import *
from pyb import *


class ModeHandler:
    """Drive mode handler:
    """

    def __init__(self):
        self.mode = -1
        self.soc = -1

    def select_drivemode(self, mode='', soc=''):
        if mode == '0' or soc > '0' and soc <= 20:
            print('eco')
            eco.activate()
            normal.toggle()
            sport.toggle()

        elif mode == '1':
            print('normal')
            eco.toggle()
            normal.activate()
            sport.toggle()

        elif mode == '2':
            print('sport')
            eco.toggle()
            normal.toggle()
            sport.activate()
        else:
            return(print("out of bounds"))

# adc instantiations
voltage_adc = ADC(Pin(ADC_VOLT_PIN))
current_adc = ADC(Pin(ADC_CURRENT_PIN))
temperature_adc = ADC(Pin(ADC_TEMP_PIN))

# ----------- Module instantiations

# initialising modes
eco = Mode(ECO_PIN)
normal = Mode(NORMAL_PIN)
sport = Mode(SPORT_PIN)
# init mode handler
mh = ModeHandler()

# init adc_address_handler

#adc_volt = ADCAddressHandler(0)
#adc_curr = ADCAddressHandler(1)
#adc_temp = ADCAddressHandler(2)
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

if __name__ == "__main__":
    pass
