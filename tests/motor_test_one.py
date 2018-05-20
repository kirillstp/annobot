import RPi.GPIO as GPIO
from time import sleep 

class MotorTest(object): 

    PINS = {'Motor1_Enable':11,
            'Motor1_Forward':13,
            'Motor1_Backward':15}

    def __init__(self):
        pass
        
    def set_pins(self):
        GPIO.setmode(GPIO.BOARD)
        for key in self.PINS.keys():
            GPIO.setup(self.PINS[key], GPIO.OUT)

    def set_forward(self):
        GPIO.output(self.PINS['Motor1_Forward'], GPIO.HIGH)
        GPIO.output(self.PINS['Motor1_Backward'], GPIO.LOW)

    def set_backward(self):
        GPIO.output(self.PINS['Motor1_Forward'], GPIO.LOW)
        GPIO.output(self.PINS['Motor1_Backward'], GPIO.HIGH)

    def set_turn_one(self):
        GPIO.output(self.PINS['Motor1_Forward'], GPIO.HIGH)
        GPIO.output(self.PINS['Motor1_Backward'], GPIO.LOW)
    
    def set_turn_two(self):
        GPIO.output(self.PINS['Motor1_Forward'], GPIO.LOW)
        GPIO.output(self.PINS['Motor1_Backward'], GPIO.LOW)

    def go(self):
        GPIO.output(self.PINS['Motor1_Enable'], GPIO.HIGH)
    
    def stop(self): 
        GPIO.output(self.PINS['Motor1_Enable'], GPIO.LOW)

    def turn_off(self):
        GPIO.cleanup()