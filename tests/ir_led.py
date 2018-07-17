#!/usr/bin/python
import RPi.GPIO as GPIO
import time
PIN=12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)
i=0
while True:
    GPIO.output(PIN, True)
    time.sleep(1)
    GPIO.output(PIN, False)
    time.sleep(1)

