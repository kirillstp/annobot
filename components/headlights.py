from sensorplatform.led import LED


class Headlights:
    def _init(self,config):
        self.headlights_config = config['headlights']
        self.headlights = LED(self.headlights_config['enable'])
    
    def toggle(self):
        LED.switch()
    
    def get_state(self):
        return 'ON' if LED.state else 'OFF'