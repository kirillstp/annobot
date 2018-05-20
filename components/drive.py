from sensorplatform import Motor


class Drivetrain:
    def __init__(self, config):
        self.motor_config = config['motor']
        self.left_motor = Motor(forward_pin = self.motor_config['left']['input1']
                                ,backward_pin = self.motor_config['left']['input2']
                                ,enable_pin = self.motor_config['left']['enable'])
        self.right_motor = Motor(forward_pin = self.motor_config['right']['input1']
                                ,backward_pin = self.motor_config['right']['input2']
                                ,enable_pin = self.motor_config['right']['enable'])
        self._running = False


    def drive_forward(self):
        self.right_motor.forward()
        self.left_motor.forward()
        self.go()

    def drive_backward(self):
        self.right_motor.backward()
        self.left_motor.backward()
        self.go()

    def turn_left(self):
        self.left_motor.stop()

    def turn_right(self):
        self.right_motor.stop()

    def go(self):
        self.right_motor.start()
        self.left_motor.start()
    
    def stop(self):
        self.right_motor.stop()
        self.left_motor.stop()