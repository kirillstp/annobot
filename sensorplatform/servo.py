from .controller import Controller, pwm

class Servo(Controller): 
    def __init__(self, pwm_pin, cycle, freq=50):
        super().__init__(name = 'servo')
        self.pwm_pin = pwm_pin
        self.set_pin_out(self.pwm_pin)
        self.cycle = cycle
        self.pwr_mgmt = pwm(self.pwm_pin, freq)
        self.set_cycle(float(cycle))

    def start(self):
        self.pwr_mgmt.start()

    def stop(self):
        self.pwr_mgmt.stop()
    
    def set_cycle(self, value):
        self.cycle = value
        self.pwr_mgmt.duty_cycle = float(self.cycle)