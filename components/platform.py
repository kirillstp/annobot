from sensorplatform.servo import Servo
import threading
from time import sleep
class Platform:
    # Two servos controlling up-down and rotation of the camera rack
    UP_DOWN_RANGE = (0.1,20) # Continious rotation servo, max - down, min - up
    ROTATE_RANGE = (2,12) # max - left, min - right
    def __init__(self, config):
        self.platform_config = config['platform']
        self.up_down = Servo(pwm_pin = self.platform_config['up_down'],
                             cycle = 0,
                             freq= 50)
        self._up_down_cycle = 0
        self.center = (max(self.ROTATE_RANGE)+min(self.ROTATE_RANGE))/2.
        self._rotate_cycle = self.center
        self.rotate = Servo(pwm_pin = self.platform_config['rotate'],
                             cycle = self.rotate_cycle,
                             freq= 50)
        self.rotate_cycle = self.center
        self.rotate_step = 1

    @property
    def rotate_cycle(self):
        return self._rotate_cycle

    @rotate_cycle.setter
    def rotate_cycle(self, value):
        self._rotate_cycle = value
        self.rotate.set_cycle(value)
        self.rotate.start()
        sleep(0.02)
        self.rotate.set_cycle(0)
        self.rotate.start()

    @property
    def up_down_cycle(self):
        return self._up_down_cycle

    @up_down_cycle.setter
    def up_down_cycle(self,value):
        self._up_down_cycle = value
        self.up_down.set_cycle(value)
        self.up_down.start()


    def rotate_left(self):
        if self.rotate_cycle < max(self.ROTATE_RANGE):
            self.rotate_cycle = self.rotate_cycle + self.rotate_step
        else:
            self.rotate_cycle = max(self.ROTATE_RANGE)

    def rotate_right(self):
        if self.rotate_cycle > min(self.ROTATE_RANGE):
            self.rotate_cycle = self.rotate_cycle - self.rotate_step
        else:
            self.rotate_cycle = min(self.ROTATE_RANGE)
    
    def up(self):
        self.up_down_cycle = max(self.UP_DOWN_RANGE)

    def down(self):
        self.up_down_cycle = min(self.UP_DOWN_RANGE)

    def stop(self):
        self.up_down_cycle = 0