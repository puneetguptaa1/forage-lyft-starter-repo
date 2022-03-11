from multiprocessing import Barrier
from Serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, battery, engine, tire):
        self.battery = battery
        self.engine = engine
        self.tire = tire

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tire.needs_service()