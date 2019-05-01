import unittest
from math import pi
from circles import circle_area

class TestCircleArea(unittest.TestCase):
    def test_normal(self):
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(2), 4*pi)

    def test_negative(self):
        self.assertRaises(ValueError, circle_area, -1)

    def test_types(self):
        self.assertRaises(TypeError, circle_area, 4.5j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "as")
