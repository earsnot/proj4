#holding constants
BATTERY_CAPACITY = 18 # [Ah] (Amp-hours)
LOWEST_SOC_THRESHOLD = 0.2
MIN_BATTERY_VOLTAGE = 42 # [Volts]
MAX_BATTERY_VOLTAGE = 52 # [Volts]
BATTERY_RESISTANCE = 0.06 # [Ohms]
R_DIS_DT_10S = 0.28 # [Ohms] (3.7V / 13.2A) - 10 second voltage drop test - From ballpark test. Resistance calculated from voltage drop over 10 seconds divided by current draw.
ADC_VOLTAGE = 3.3 # [Volts]
ECO_PIN = 'X1'
NORMAL_PIN = 'X2'
SPORT_PIN = 'X3'


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
