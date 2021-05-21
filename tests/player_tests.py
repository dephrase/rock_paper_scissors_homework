import unittest
from classes.player import Player

class testPlayer(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("David", "Rock")

    def test_player_has_name(self):
        self.assertEqual("David", self.player1.name)

    def test_player_has_choice(self):
        self.assertEqual("Rock", self.player1.choice)