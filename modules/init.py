# dump init stuff here
from pyb import Pin, ADC
import modules.drivemodes
import libs.constants

#def do_readings():
#    readings = [voltage="", current="", temperature=""]
#    readings.append(voltage="", voltage_adc.read())
 #   readings.append(current="", current_adc.read())
    


def init():
    # initialising ADCs
    voltage_adc = ADC(Pin(ADC_VOLT_PIN))
    current_adc = ADC(Pin(ADC_CURRENT_PIN))
    temperature_adc = ADC(Pin(ADC_TEMP_PIN))
    
    # initialising modes
    eco = Mode(ECO)
    normal = Mode(NORMAL)
    sport = Mode(SPORT)
    
    # init mode handler
    mh = ModeHandler()
    # init adc_address_handler
    adcadc = ADCAddressHandler()
    adcadc.set_address(0)
    



    adc_volt = ADCAddressHandler(0)
    adc_curr = ADCAddressHandler(1)
    adc_temp = ADCAddressHandler(2)

    adc_volt.get_address()
    adc_curr.get_address()






print(eco)