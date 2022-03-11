from tire.tire import Tire

class octoprime(Tire):
    def __init__(self, tire_array):
        self.tire_array = tire_array

    def needs_service(self):
        return sum(self.tire_array) >= 3.0