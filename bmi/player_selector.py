from bmi.bmi_calculator import BmiCalculator


class PlayerSelector(object):
    def check_height(self, player):
        if player['height_in_ft'] <= 5 and player['height_in_in'] <= 7:
            return 'Player is too short'
        elif player['height_in_ft'] >= 6 and player['height_in_in'] >= 5:
            return 'Player is too tall'
        else:
            return 'Player is ok'

    def check_weight(self, player):
        if player['weight_in_lbs'] <= 141:
            return 'Player is too light'
        elif player['weight_in_lbs'] >= 290:
            return 'Player is too fat'
        else:
            return 'Player weight is ok'

    def check_bmi(self, player):
        bmi_calculator = BmiCalculator()
        player_ft = player['height_in_ft']
        player_in = player['height_in_in']
        player_lbs = player['weight_in_lbs']
        player_bmi = bmi_calculator.calculate_bmi(player_ft, player_in, player_lbs)
        if player_bmi <= 21.1:
            return 'Bmi value is too low'
        elif player_bmi >= 25.8:
            return 'Bmi value is too high'
        else:
            return 'Bmi value is ok'


