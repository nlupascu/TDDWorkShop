class HeightCalculator(object):
    def convert_inches_to_cm(self, height_in_inches):
        return height_in_inches * 2.54

    def convert_ft_to_inch(self, height_in_ft):
        return height_in_ft * 12

    # def convert_ft_to_cm(self, height_in_ft):
    #     height_in_inches = self.convert_ft_to_inch(height_in_ft)
    #     height_in_cm = self.convert_inches_to_cm(height_in_inches)
    #     return height_in_cm

    def convert_ft_and_inch_to_inch(self, ft, inches):
        calculated_inches = self.convert_ft_to_inch(ft)
        return calculated_inches + inches

    # def convert_ft_and inch_to_cm(self, ft, inches):
    #     calculated_cm = self.convert_ft_to_cm()

    def convert_ft_and_inch_to_cm(self, ft, inch):
        calculated_inch = self.convert_ft_and_inch_to_inch(ft, inch)
        return self.convert_inches_to_cm(calculated_inch)

    def convert_ft_and_inch_to_m(self, ft, inch):
        calculated_m = self.convert_ft_and_inch_to_cm(ft, inch) / 100
        return calculated_m