import unittest
from datetime import date

from engine.capulet_engine import capulet

class testNubbin(unittest.TestCase):
    def test_needs_service(self):
        current_mileage = 7892
        last_service_mileage = 1359
        engine = capulet(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_doesnt_need_service(self):
        current_mileage = 7892
        last_service_mileage = 7000
        engine = capulet(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())