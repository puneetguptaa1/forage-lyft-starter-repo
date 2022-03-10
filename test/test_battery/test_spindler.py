import unittest
from datetime import date

from battery.spindlerBattery import spindler

class testSpindler(unittest.TestCase):
    def test_needs_service(self):
        current_date = date.fromisoformat("2016-06-01")
        last_service_date = date.fromisoformat("2014-03-01")
        battery = spindler(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_doesnt_need_service(self):
        current_date = date.fromisoformat("2016-06-01")
        last_service_date = date.fromisoformat("2014-10-01")
        battery = spindler(current_date, last_service_date)
        self.assertFalse(battery.needs_service())