from config.configuration import Config
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

def cleanup():
    GPIO.cleanup()

class Controller:

    def __init__(self, name):
        super().__init__(self)
        self._name = name
        GPIO.setmode(GPIO.BOARD) #should create singleton that initializes GPPIO?? or noot, dont know

    def set_pin_out(self, pin):
        GPIO.setup(self.PINS[key], GPIO.OUT)

    def set_pin_in(self, pin):
        GPIO.setup(pin, GPIO.IN)

    def send_to_pin(self, pin, on = False):
        send = GPIO.HIGH if on else GPIO.LOW
        GPIO.output(pin, send)
    