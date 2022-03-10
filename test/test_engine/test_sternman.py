import unittest
from datetime import date

from engine.sternman_engine import sternman

class testNubbin(unittest.TestCase):
    def test_needs_service(self):
        warning_light = True
        engine = sternman(warning_light)
        self.assertTrue(engine.needs_service())

    def test_doesnt_need_service(self):
        warning_light = False
        engine = sternman(warning_light)
        self.assertFalse(engine.needs_service())