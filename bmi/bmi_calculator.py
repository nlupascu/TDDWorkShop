from bmi.height_calculator import HeightCalculator
from bmi.weight_calculator import WeightCalculator


class BmiCalculator(object):

    def calculate_bmi(self, ft, inch, pounds):

        height_calculator = HeightCalculator()
        weight_calculator = WeightCalculator()

        height_in_m = height_calculator.convert_ft_and_inch_to_m(ft, inch)
        height_in_m_squared = height_in_m ** 2
        weight_in_kg = weight_calculator.convert_pounds_to_kg(pounds)
        bmi = weight_in_kg/height_in_m_squared

        return bmi

