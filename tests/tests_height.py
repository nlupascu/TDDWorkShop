from unittest import TestCase

from bmi.height_calculator import HeightCalculator


class HeightTests(TestCase):

    def setUp(self):
        self.height_calculator = HeightCalculator()

    def test_convert_one_inch_in_cm(self):
        #pass # it is used to fill empty functions/class, use it when empty
        self.assertEqual(2.54, self.height_calculator.convert_inches_to_cm(1))

    def test_convert_two_inches_in_cm(self):
        self.assertEqual(5.08, self.height_calculator.convert_inches_to_cm(2))

    def test_convert_3_inches_in_cm(self):
        self.assertEqual(7.62, self.height_calculator.convert_inches_to_cm(3))

    def test_convert_one_ft_in_inch(self):
        self.assertEqual(12, self.height_calculator.convert_ft_to_inch(1))

    def test_convert_two_ft_in_inches(self):
        self.assertEqual(24, self.height_calculator.convert_ft_to_inch(2))

    def test_convert_3_ft_in_inches(self):
        self.assertEqual(36, self.height_calculator.convert_ft_to_inch(3))

    # def test_convert_one_ft_to_cm(self):
    #     self.assertEqual(30.48, self.height_calculator.convert_ft_to_cm(1))
    #
    # def test_convert_two_ft_to_cm(self):
    #     self.assertEqual(60.96, self.height_calculator.convert_ft_to_cm(2))
    #
    # def test_convert_3_ft_to_cm(self):
    #     self.assertEqual(91.44, self.height_calculator.convert_ft_to_cm(3))

    def test_convert_one_ft_one_inch_to_inches(self):
        self.assertEqual(13, self.height_calculator.convert_ft_and_inch_to_inch(1, 1))

    def test_convert_one_ft_2_inches_to_inches(self):
        self.assertEqual(14, self.height_calculator.convert_ft_and_inch_to_inch(1, 2))

    def test_convert_2_ft_2_inches_to_inches(self):
        self.assertEqual(26, self.height_calculator.convert_ft_and_inch_to_inch(2, 2))

    def test_convert_ft_and_inches_to_cm(self):
        self.assertEqual(33.02, self.height_calculator.convert_ft_and_inch_to_cm(1, 1))

    def test_convert_ft_and_inch_to_m(self):
        self.assertEqual(0.33020000000000005, self.height_calculator.convert_ft_and_inch_to_m(1, 1))