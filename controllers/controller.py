from app import app
from classes.game import Game
from classes.player import Player
from flask import render_template, request, redirect, session, url_for

@app.route('/')
def index():
    return render_template('index.html', title='Rock Paper Scissors')
    
@app.route('/rules')
def view_rules():
    return render_template('rules.html', title='Rules')

@app.route('/play-against-player')
def player_versus_player():
    return render_template('play-against-player.html', title='Play against player')

@app.route('/play-against-computer')
def play_against_computer():
    return render_template('play-against-computer.html', title='Play Against Computer')

@app.route('/winner/<winner>')
def display_result(winner):
    return render_template('winner.html', winner=winner)
    
@app.route('/winner', methods=['GET', 'POST'])
def add_winner_to_page():
    player1_name = request.form['player1-name']
    player1_choice = request.form['player1-choice']
    player2_name = request.form['player2-name']
    player2_choice = request.form['player2-choice']
    new_game = Game("Game 1")
    player1 = Player(player1_name, player1_choice)
    player2 = Player(player2_name, player2_choice)
    result = new_game.play_game(player1, player2)
    if result == "Draw":
        winner = "Draw"
    else:
        winner = result.name  
    return redirect(url_for('display_result', winner=winner))

@app.route('/winner-computer', methods=['GET', 'POST'])
def get_computer_winner():
    newgame = Game("Game")
    player1_name = request.form['player1name']
    player1_choice = request.form['player1choice']
    computername = "computer"
    computerchoice = newgame.get_computer_choice()
    player1 = Player(player1_name, player1_choice)
    computer = Player(computername, computerchoice)
    result = newgame.play_game(player1, computer)
    if result == "Draw":
        winner = "Draw"
    else:
        winner = result.name
    return redirect(url_for('display_result', winner=winner))