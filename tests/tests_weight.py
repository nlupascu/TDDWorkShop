from unittest.case import TestCase

from bmi.weight_calculator import WeightCalculator


class WeightTests(TestCase):

    def setUp(self):
        self.weight_calculator = WeightCalculator()

    def test_convert_one_pound_to_kg(self):
        self.assertEqual(0.45359237, self.weight_calculator.convert_pounds_to_kg(1))


    def test_convert_2_pounds_to_kg(self):
        self.assertEqual(0.90718474, self.weight_calculator.convert_pounds_to_kg(2))
