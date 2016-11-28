from unittest.case import TestCase

from bmi.player_selector import PlayerSelector



class PlayerSelectionTests(TestCase):
    def setUp(self):
        self.player_selector = PlayerSelector()
        self.player = {'height_in_ft': 5, 'height_in_in': 0, 'weight_in_lbs': 175}

    def test_player_too_short(self):
        self.assertEqual('Player is too short', self.player_selector.check_height(self.player))

    def test_player_too_tall(self):
        self.player['height_in_ft'] = 6
        self.player['height_in_in'] = 6
        self.assertEqual('Player is too tall', self.player_selector.check_height(self.player))

    def test_player_ok(self):
        self.player['height_in_ft'] = 5
        self.player['height_in_in'] = 9
        self.assertEqual('Player is ok', self.player_selector.check_height(self.player))

    def test_player_too_light(self):
        self.player['weight_in_lbs'] = 141
        self.assertEqual('Player is too light', self.player_selector.check_weight(self.player))

    def test_player_too_fat(self):
        self.player['weight_in_lbs'] = 290
        self.assertEqual('Player is too fat', self.player_selector.check_weight(self.player))

    def test_player_weight_ok(self):
        self.player['weight_in_lbs'] = 189
        self.assertEqual('Player weight is ok', self.player_selector.check_weight(self.player))

    def test_player_bmi_too_low(self):
        self.player['height_in_ft'] = 5
        self.player['height_in_in'] = 1
        self.player['weight_in_lbs'] = 89
        self.assertEqual('Bmi value is too low', self.player_selector.check_bmi(self.player))

    def test_player_bmi_too_high(self):
        self.player['height_in_ft'] = 5
        self.player['height_in_in'] = 1
        self.player['weight_in_lbs'] = 178
        self.assertEqual('Bmi value is too high', self.player_selector.check_bmi(self.player))

    def test_player_bmi_ok(self):
        self.player['height_in_ft'] = 5
        self.player['height_in_in'] = 2
        self.player['weight_in_lbs'] = 120
        self.assertEqual('Bmi value is ok', self.player_selector.check_bmi(self.player))


