from .controller import Controller, pwm

class Motor(Controller): 
    def __init__(self, phase_pin, enable_pin, power_percent):
        super().__init__(name = 'motor')
        self.phase_pin = phase_pin
        self.enable_pin = enable_pin
        self.set_pin_out(self.phase_pin)
        self.set_pin_out(self.enable_pin)
        self.pwr_mgmt = pwm(self.enable_pin, 1000)
        self.pwr_mgmt.duty_cycle = float(power_percent)

    def forward(self):
        self.send_to_pin(self.phase_pin, on = True)
        
    def backward(self):
        self.send_to_pin(self.phase_pin, on = False)

    def start(self):
        self.pwr_mgmt.start()
    
    def stop(self):
        self.pwr_mgmt.stop()