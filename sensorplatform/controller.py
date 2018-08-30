import RPi.GPIO as GPIO

GPIO.setwarnings(False)

def cleanup():
    GPIO.cleanup()

class Controller:

    def __init__(self, name):
        self._name = name
        self._duty_cycle = 100
        GPIO.setmode(GPIO.BOARD) #should create singleton that initializes GPPIO?? or noot, dont know

    def set_pin_out(self, pin):
        # print ("setting pin {} to out".format(pin))
        GPIO.setup(int(pin), GPIO.OUT)

    def set_pin_in(self, pin):
        # print ("setting pin {} to in".format(pin))
        GPIO.setup(int(pin), GPIO.IN)

    def send_to_pin(self, pin, on = False):
        send = GPIO.HIGH if on else GPIO.LOW
        GPIO.output(int(pin), send)
    
class pwm:
    def __init__(self, pin, hz):
        self._pin = int(pin) 
        self._pwm_ctrl = GPIO.PWM(self._pin,int(hz))
        self._duty_cycle = 100
    
    def start(self):
        self._pwm_ctrl.start(self.duty_cycle)

    def stop(self):
        self._pwm_ctrl.stop()

    @property
    def duty_cycle(self):
        return self._duty_cycle
    
    @duty_cycle.setter
    def duty_cycle(self, value):
        self._pwm_ctrl.ChangeDutyCycle(value)
        print("DUTY CYCLE SET {}".format(value))
        self._duty_cycle = value