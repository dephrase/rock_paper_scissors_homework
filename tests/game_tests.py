import unittest
from classes.player import Player
from classes.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game("Game 1")

    def test_game_has_name(self):
        self.assertEqual("Game 1", self.game.name)

    def test_player1_beats_player2_with_rock(self):
        player1 = Player("David", "Rock")
        player2 = Player("Craig", "Scissors")
        self.assertEqual(player1, self.game.play_game(player1, player2))

    def test_player1_beats_player2_with_paper(self):
        player1 = Player("David", "Paper")
        player2 = Player("Craig", "Rock")
        self.assertEqual(player1, self.game.play_game(player1, player2))

    def test_player1_beats_player2_with_scissors(self):
        player1 = Player("David", "Scissors")
        player2 = Player("Craig", "Paper")
        self.assertEqual(player1, self.game.play_game(player1, player2))

    def test_player_2_wins_with_paper(self):
        player1 = Player("David", "Rock")
        player2 = Player("Craig", "Paper")
        self.assertEqual(player2, self.game.play_game(player1, player2))

    def test_game_can_be_a_draw(self):
        player1 = Player("David", "Rock")
        player2 = Player("Craig", "Rock")
        self.assertEqual(None, self.game.play_game(player1, player2))