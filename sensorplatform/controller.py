import RPi.GPIO as GPIO

GPIO.setwarnings(False)

def cleanup():
    GPIO.cleanup()

class Controller:

    def __init__(self, name):
        self._name = name
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
    