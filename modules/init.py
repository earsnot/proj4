# dump init stuff here
#from pyb import Pin, ADC
from modules import Mode, ModeHandler
import libs.constants

#def do_readings():
#    readings = [voltage="", current="", temperature=""]
#    readings.append(voltage="", voltage_adc.read())
 #   readings.append(current="", current_adc.read())
    

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
    
    # init mode handler
    mh = ModeHandler()

    # init adc_address_handler
    adc_volt = ADCAddressHandler(0)
    adc_curr = ADCAddressHandler(1)
    adc_temp = ADCAddressHandler(2)

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

