from tkinter import E
from battery import battery
from car import Car
from battery.nubbinBattery import nubbin
from battery.spindlerBattery import spindler
from engine.capulet_engine import capulet
from engine.sternman_engine import sternman
from engine.willoughby_engine import willoughby

class factory:
    @staticmethod
    def build_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        battery = spindler(current_date, last_service_date)
        engine = capulet(current_mileage, last_service_mileage)        
        car = Car(battery, engine)
        return car
    
    @staticmethod
    def build_glissade(current_date, last_service_date, service_light_on):
        battery = spindler(current_date, last_service_date)
        engine = sternman(service_light_on)        
        car = Car(battery, engine)
        return car

    @staticmethod
    def build_palindrome(current_date, last_service_date, current_mileage, last_service_mileage):
        battery = spindler(current_date, last_service_date)
        engine = capulet(current_mileage, last_service_mileage)        
        car = Car(battery, engine)
        return car

    @staticmethod
    def build_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        battery = nubbin(current_date, last_service_date)
        engine = willoughby(current_mileage, last_service_mileage)        
        car = Car(battery, engine)
        return car

    @staticmethod
    def build_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        battery = nubbin(current_date, last_service_date)
        engine = capulet(current_mileage, last_service_mileage)
        car = Car(engine, battery)
        return car