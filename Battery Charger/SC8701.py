from machine import pin, PWM
from numpy import clip

class SC8701:
    def __init__(self, VPWM_pin, IPWM_pin, max_voltage, max_current):
        self.max_voltage = max_voltage
        self.max_current = max_current

        VPWM = PWM(Pin(VPWM_pin))
        VPWM.freq(25_000_000_000)               # 25Mhz
        VPWM.duty_u16(0)                        # set duty cycle to zero to ensure no output

        IPWM = PWM(Pin(IPWM_pin))
        IPWM.freq(25_000_000_000)               # 25Mhz
        IPWM.duty_u16(0)                        # set duty cycle to zero to ensure no output

    def set_output_voltage(self, voltage):
        pass

    def set_output_current(self, current):
        IPWM_duty_cycle = clip(current / self.max_current, 0, 1)
        self.IPWM.duty_u16(current * 65535)
    
    def read_input_voltage(self):
        pass

    def read_battery_voltage(self):
        pass

    def read_output_current(self):
        pass