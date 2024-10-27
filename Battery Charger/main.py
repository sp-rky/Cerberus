from machine import PWM, Pin, ADC
from numpy import clip
from time import sleep

# import support files
import OLED
import SC8701

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

# set up SC8701
buck_boost = SC8701.SC8701(2, 3, SC8701_max_voltage, SC8701_max_current)

# set up OLED display
oled = OLED.OLED()

while 1:
    if not charging:
        # get the VIN and VBAT voltages
        VBAT = buck_boost.read_battery_voltage()
        VIN = buck_boost.read_input_voltage()
        
        # update the OLED display
        oled.update(False, VBAT, VIN, 0, 0, 0)

        if VIN > 5:
            charging = True
    
    else:
        # get the VIN and VBAT voltages
        VBAT = buck_boost.read_battery_voltage()
        VIN = buck_boost.read_input_voltage()

        # start with a small pre-charge to get the battery ready for CC charging
        if VBAT / battery_cell_count < 3.1:
            # ramp up the charging voltage slowly over 250 seconds
            for battery_charge_voltage in range(3.5, 4.0, 0.0005):
                charging_current = 0.1 * battery_capacity
                buck_boost.set_output_current(charging_current)
                buck_boost.set_output_voltage(battery_charge_voltage * battery_cell_count)

                time.sleep(0.25)
            # stop the precharge and check the cell voltage
            buck_boost.set_output_voltage(0)
            time.sleep(5)
            VBAT = buck_boost.read_battery_voltage()

            # if the voltage is still low, then continue a low current charge until it goes above 3.1V
            while VBAT / battery_cell_count < 3.1:
                buck_boost.set_output_voltage(4 * battery_cell_count)
                time.sleep(30)
                buck_boost.set_output_voltage(0)
                time.sleep(5)
                VBAT = buck_boost.read_battery_voltage()

        # otherwise, begin constant current charge
        if VBAT / battery_cell_count < 3.6 and VBAT / battery_cell_count > 3.1 :
            charging_current = battery_max_charge_rate * battery_capacity
            buck_boost.set_output_current(charging_current)
            




