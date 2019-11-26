# holding constants
LOWEST_THRESHOLD = 20 # [%] 
ADC_VOLTAGE = 3.3 # [Volt] 
# adc pins
ADC_VOLTAGE_PIN = 'X19'
ADC_CURRENT = 'X20'
ADC_TEMPERATURE = 'X21'
# pins for drive mode selection

#holding constants
BATTERY_CAPACITY = 18 # [Ah] (Amp-hours)
MIN_BATTERY_VOLTAGE = 42 # [Volts]
MAX_BATTERY_VOLTAGE = 52 # [Volts]
BATTERY_RESISTANCE = 0.06 # [Ohms]
R_DIS_DT_10S = 0.28 # [Ohms] (3.7V / 13.2A) - 10 second voltage drop test - From ballpark test. Resistance calculated from voltage drop over 10 seconds divided by current draw.
ECO_PIN = 'x1'
NORMAL_PIN = 'x2'
SPORT_PIN = 'x3'


# --- SENSORS ---
# temperature
MIN_TEMP_SENSOR = 10
MAX_TEMP_SENSOR = 60
TYPE_TEMP_SENSOR = 0

# current
MIN_CURENT_SENSOR = 0
MAX_CURENT_SENSOR = 22
TYPE_CURENT_SENSOR = 1

# voltage
MIN_VOLT_SENSOR = 35
MAX_VOLT_SENSOR = 55
TYPE_VOLT_SENSOR = 2
