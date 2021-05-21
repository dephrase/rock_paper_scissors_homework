from app import app

@app.route('/')
def print_hello():
    return "Hello World"

@app.route('/<player1Choice>/<player2Choice>')
def calculate_winner(player1Choice, player2Choice):
    player1 = player1Choice.lower()
    player2 = player2Choice.lower()

