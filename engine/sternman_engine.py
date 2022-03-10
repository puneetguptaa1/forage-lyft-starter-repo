from engine import engine

class sternman(engine):
    def __init__(self, warning_light):
        # if true, warning light on, else false
        self.warning_light = warning_light
    
    def needs_service(self):
        return self.warning_light
