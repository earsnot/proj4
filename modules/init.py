# dump init stuff here
from pyb import Pin, ADC
import drivemodes
import libs.constants

def init():
    # initialising ADCs
    voltage_adc = ADC(Pin(ADC_VOLT_PIN))
    current_adc = ADC(Pin(ADC_CURRENT_PIN))
    temperature_adc = ADC(Pin(ADC_TEMP_PIN))
    
    # initialising modes
    eco = Mode(ECO)
    normal = Mode(NORMAL)
    sport = Mode(SPORT)







print(eco)