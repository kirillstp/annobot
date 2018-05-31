from sensorplatform.led import LED


class Headlights:
    def __init__(self,config):
        self.headlights_config = config['headlights']
        self.headlights = LED(self.headlights_config['enable'])
    
    def toggle(self):
        self.headlights.switch()
    
    def get_state(self):
        return 'ON' if self.headlights.state else 'OFF'