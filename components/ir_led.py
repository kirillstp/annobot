import subprocess
from time import sleep
class IRLED: 
    # IR LED class is a weirdo:
    #   - does a wtf Popen call to irrp.py since i do not have time to refactor irrp.py
    #           (HINT: Irrp.py written with a f***** argparser and bagillion args)
    #   - uses BCM pin # on RPi instead of board # since i do not have time to refactor irrp.py

    def __init__(self,config):
        self.ir_led_pin = config["ir_led"]["enable"]
        self.pigpiod = subprocess.call(['sudo', 'pigpiod'])

    def run_code(self, code):
        # code options: mute, power, v_down, v_up, power_test
        # for more info see ir_codes
        # E.g ./irrp.py -p -g 18 -f ir_codes mute
        run = subprocess.Popen(['./irrp.py', '-p', '-g', str(self.ir_led_pin), '-f', 'ir_codes', code])
