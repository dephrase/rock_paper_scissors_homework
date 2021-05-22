from logging import debug
from flask import Flask

app = Flask(__name__)

from controllers import controller

app.secret_key = 'What is a secret key?'

if __name__ == "__main__":
    app.run(debug=True)