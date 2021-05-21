from classes.player import Player
from classes import *

class Game:
    def __init__(self, name):
        self.name = name

    def play_game(self, player1, player2):
        player1choice = player1.choice.lower()
        player2choice = player2.choice.lower()

        if player1choice == "rock" and player2choice == "scissors":
            return player1
        elif player1choice == "scissors" and player2choice == "paper":
            return player1
        elif player1choice == "paper" and player2choice == "rock":
            return player1
        elif player1choice == "rock" and player2choice == "paper":
            return player2
        elif player1choice == "scissors" and player2choice == "rock":
            return player2
        elif player1choice == "paper" and player2choice == "scissors":
            return player2
        elif player1choice == player2choice:
            return None