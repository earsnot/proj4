# Settings
SOC_LOW_THRESHOLD = 20 # [%]
AVG_WINDOW_SIZE = 30
INTERRUPT_FREQ = 1
INTERRUPT_TIME = 1/INTERRUPT_FREQ

# Adc pins
ADC_VOLT_PIN = 'X19'
ADC_CURRENT_PIN = 'X20'
ADC_TEMP_PIN = 'X21'

# Pins for drive mode selection
ECO_PIN = 'X1'
NORMAL_PIN = 'X2'
SPORT_PIN = 'X3'


# PyBoard settings
ADC_VOLTAGE = 3.3 # [Volt]
ADC_BIT_SETTING = 12 # PyBoard v1.1 ADC is 12 bit

# Battery specs
BATTERY_CAPACITY = 18 # [Ah] (Amp-hours)
MIN_BATTERY_VOLTAGE = 42 # [Volts]
MAX_BATTERY_VOLTAGE = 52 # [Volts]
BATTERY_RESISTANCE = 0.06 # [Ohms]
R_DIS_DT_10S = 0.28 # [Ohms] (3.7V / 13.2A) - 10 second voltage drop test - From ballpark test. Resistance calculated
                    # from voltage drop over 10 seconds divided by current draw.

# Scalers
VOLT_DIV_SCALE = 14.86 # (( HVAD ER VORES VOLTAGE DIVIDER SCALING FOR SPÆNDINGSMÅLING!? ))
CURR_DIV_SCALE = 4 # (( HVAD ER VORES VOLTAGE DIVIDER SCALING FOR STRØMMÅLING!? ))


# Functions
SOC_SLOPE = 0 # These should be defined
SOC_INTERCEPT = 0 # These should be defined
HALL_SEN_SLOPE = 0 # These should be defined
HALL_SEN_INTERCEPT = 0 # These should be defined

# --- SENSORS ---
# Temperature
MIN_TEMP_SENSOR = 10
MAX_TEMP_SENSOR = 60
TYPE_TEMP_SENSOR = 0

# Current
MIN_CURRENT_SENSOR = 0
MAX_CURRENT_SENSOR = 22
TYPE_CURRENT_SENSOR = 1

# Voltage
MIN_VOLT_SENSOR = 35
MAX_VOLT_SENSOR = 55
TYPE_VOLT_SENSOR = 2
