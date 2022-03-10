from battery.battery import Battery
from date import date_change

class nubbin(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date
    
    def needs_service(self):
        service_by_date = date_change(self.last_service_date, 4)
        if (service_by_date < self.current_date):
            return True
        else:
            return False
