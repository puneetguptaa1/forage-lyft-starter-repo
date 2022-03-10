import unittest
from datetime import date

from battery.nubbinBattery import nubbin

class testNubbin(unittest.TestCase):
    def test_needs_service(self):
        current_date = date.fromisoformat("2016-06-01")
        last_service_date = date.fromisoformat("2010-03-01")
        battery = nubbin(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_doesnt_need_service(self):
        current_date = date.fromisoformat("2016-06-01")
        last_service_date = date.fromisoformat("2013-03-01")
        battery = nubbin(current_date, last_service_date)
        self.assertFalse(battery.needs_service())