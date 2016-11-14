from unittest.case import TestCase

from bmi.bmi_calculator import BmiCalculator


class BmiTest(TestCase):
    def setUp(self):
        self.bmi_calculator = BmiCalculator()

    def test_calculate_5ft_9inch_141lbs(self):
        self.assertEqual(20.821846403932255, self.bmi_calculator.calculate_bmi(5, 9, 141))

    def test_calculate_5ft_9inch_174lbs(self):
        self.assertEqual(25.695044498469592, self.bmi_calculator.calculate_bmi(5, 9, 174))

    def test_calculate_7ft_8inch_190lbs(self):
        self.assertEqual(15.782516556172052, self.bmi_calculator.calculate_bmi(7, 8, 190))

    def test_calculate_5ft_5inch_120lbs(self):
        self.assertEqual(19.968840131763105, self.bmi_calculator.calculate_bmi(5, 5, 120))