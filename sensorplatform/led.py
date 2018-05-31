from .controller import Controller, pwm

class LED(Controller): 
    # For example: headlights use one GPIO pin wired to B pin of NPN transistor to turn on two LED lights rated at 3V
    def __init__(self, enable_pin):
        self.enable_pin = enable_pin
        self.set_pin_out(self.enable_pin)
        self._toggle = False
        self.send_to_pin(self.enable_pin, on = self._toggle)
    
    def switch(self):
        self._toggle = not self._toggle
        self.send_to_pin(self.enable_pin, on = self._toggle)
    
    @property
    def state(self):
        return self._toggle

    @state.setter
    def state(self,value):
        self._toggle = value
        self.send_to_pin(self.enable_pin, on = self._toggle)