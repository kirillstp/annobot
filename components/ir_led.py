import subprocess
from time import sleep
class IRLED: 
    # Configure lirc:
    # Copy hardware.conf to /etc/lirc/hardware.conf
    # In /etc/modules add:
    #       lirc_dev
    #       lirc_rpi gpio_in_pin=23 gpio_out_pin=22
    # In /boot/config.txt add:
    #       dtoverlay=lirc-rpi,gpio_in_pin=23,gpio_out_pin=22
    # In /etc/lirc/lirc_options.conf change driver to default
    # To use:
    # irsend SEND_ONCE toshiba KEY_POWER


    def __init__(self,config):
        pass

    def run_code(self, code):
        # code options /etc/lirc/lircd.conf.d/
        run = subprocess.Popen(['irsend', 'SEND_ONCE', 'toshiba', str(code)])
