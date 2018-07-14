from sensorplatform.motor import Motor


class Drivetrain:
    def __init__(self, config):
        self.motor_config = config['motor']
        self.left_motor = Motor(phase_pin = self.motor_config['left']['phase']
                                ,enable_pin = self.motor_config['left']['enable']
                                ,power_percent = self.motor_config['left']['power_percent'])
        self.right_motor = Motor(phase_pin = self.motor_config['right']['phase']
                                ,enable_pin = self.motor_config['right']['enable']
                                ,power_percent = self.motor_config['right']['power_percent'])
        self._running = False


    def drive_forward(self):
        self.left_motor.forward()
        self.right_motor.forward()
        self.go()

    def drive_backward(self):
        self.left_motor.backward()
        self.right_motor.backward()
        self.go()

    def turn_left(self):
        self.right_motor.forward()
        self.left_motor.backward()

    def turn_right(self):
        self.left_motor.forward()
        self.right_motor.backward()

    def go(self):
        self.right_motor.start()
        self.left_motor.start()
    
    def stop(self):
        self.right_motor.stop()
        self.left_motor.stop()