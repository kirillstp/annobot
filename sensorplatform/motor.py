from .controller import Controller

class Motor(Controller): 
    def __init__(self, forward_pin, backward_pin, enable_pin):
        super().__init__(name = 'motor')
        self.forward_pin = forward_pin
        self.backward_pin = backward_pin
        self.enable_pin = enable_pin
        self.set_pin_out(self.forward_pin)
        self.set_pin_out(self.backward_pin)
        self.set_pin_out(self.enable_pin)

    def forward(self):
        self.send_to_pin(self.backward_pin, on = False)
        self.send_to_pin(self.forward_pin, on = True)
    
    def backward(self):
        self.send_to_pin(self.forward_pin, on = False)
        self.send_to_pin(self.backward_pin, on = True)

    def start(self):
        self.send_to_pin(self.enable_pin, on = True)
    
    def stop(self):
        self.send_to_pin(self.enable_pin, on = False)