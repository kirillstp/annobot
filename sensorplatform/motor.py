from .controller import Controller, pwm

class Motor(Controller): 
    def __init__(self, forward_pin, backward_pin, enable_pin, power_percent):
        super().__init__(name = 'motor')
        self.forward_pin = forward_pin
        self.backward_pin = backward_pin
        self.enable_pin = enable_pin
        self.set_pin_out(self.forward_pin)
        self.set_pin_out(self.backward_pin)
        self.set_pin_out(self.enable_pin)
        self.pwr_mgmt = pwm(self.enable_pin,500)
        self.pwr_mgmt.duty_cycle = float(power_percent)

    def forward(self):
        self.send_to_pin(self.backward_pin, on = False)
        # print("Forward Pin {} True".format(self.forward_pin))
        self.send_to_pin(self.forward_pin, on = True)
        # print("Backward Pin {} False".format(self.backward_pin))
        
    
    def backward(self):
        self.send_to_pin(self.forward_pin, on = False)
        # print("Forward Pin {} False".format(self.forward_pin))
        self.send_to_pin(self.backward_pin, on = True)
        # print("Backward Pin {} True".format(self.backward_pin))

    def start(self):
        self.pwr_mgmt.start()
    
    def stop(self):
        self.pwr_mgmt.stop()