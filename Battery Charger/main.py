from machine import PWM, Pin, ADC

# config options:
SC8701_max_voltage = 15                     # max voltage of buck-boost (in volts) at 100% duty cycle (if you adjust the voltage trimpot, calibrate this!)
SC8701_max_current = 10                     # max current of buck-boost (in amps) at 100% duty cycle (if you adjust the current trimpot, calibrate this!)
battery_cell_count = 1                      # cell count of battery 
battery_capacity = 0.6                      # battery capacity (in amp-hours)
battery_max_charge_rate = 0.5               # max charge rate (in c, i.e. charge battery of X capacity at X * c Amps)
VBAT_calibration = 2.6                      # what voltage is read at VBAT_pin when input to the voltage divider is 5V
VIN_calibration = 2.6                       # what voltage is read at VBAT_pin when input to the voltage divider is 5V

# loop variables
charging = False
waiting = True
conversion_factor = 3.3 / (65535)
VBAT = 0
VIN = 0

# setup PWM control for voltage and current
VPWM_pin = PWM(Pin(2))
VPWM_pin.freq(25_000_000_000)               # 25Mhz
VPWM_pin.duty_u16(0)                        # set duty cycle to zero to ensure no output

IPWM_pin = PWM(Pin(3))
IPWM_pin.freq(25_000_000_000)               # 25Mhz
IPWM_pin.duty_u16(0)                        # set duty cycle to zero to ensure no output

# set up other input pins
VBAT_pin = ADC(3)
VIN_pin = ADC(4)

while (1):
    while (waiting):
        VBAT = VBAT_pin.read_u16() * conversion_factor
        VIN = VIN_pin.read_u16() * 




