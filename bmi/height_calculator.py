class HeightCalculator(object):
    def convert_inches_to_cm(self, height_in_inches):
        return height_in_inches * 2.54

    def convert_ft_to_inch(self, height_in_ft):
        return height_in_ft * 12

    def convert_ft_to_cm(self, height_in_ft):
        height_in_inches = self.convert_ft_to_inch(height_in_ft)
        height_in_cm = self.convert_inches_to_cm(height_in_inches)
        return height_in_cm

    def convert_ft_and_inch_to_inch(self, ft, inches):
        calculated_inches = self.convert_ft_to_inch(ft)
        return calculated_inches + inches