from app import app
from classes.game import Game
from classes.player import Player
from flask import render_template, request, redirect

@app.route('/')
def index():
    return render_template('index.html', title='Rock Paper Scissors')
    
@app.route('/rules')
def view_rules():
    return render_template('rules.html', title='Rules')

@app.route('/play-against-player')
def player_versus_player():
    return render_template('play-against-player.html')

# @app.route('/winner')
# def display_result():
#     return render_template('winner.html', title="Result")
    
@app.route('/winner', methods=['POST'])
def add_winner_to_page():
    if request == 'POST':
        player1_name = request.form['player1-name']
        player1_choice = request.form['player1-choice']
        player2_name = request.form['player2-name']
        player2_choice = request.form['player2-choice']
        new_game = Game("Game 1")
        player1 = Player(player1_name, player1_choice)
        player2 = Player(player2_name, player2_choice)
        result = new_game.play_game(player1, player2)
        if type(result) == None:
            winner = "Draw"
        else:
            winner = result.name
        redirect('/winner.html')
    else:
        return render_template('/display_winner.html', title="Result", winner=winner)
        

@app.route('/display_winner')
def display_winner(winner):
    return render_template('display_winner.html', title='Winner', winner=winner)

