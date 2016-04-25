from flask import Flask
from flask import request
import engine

app = Flask(__name__)

@app.route("/")
def menu():
    return open('menu.html').read()

@app.route("/game")
def game():
    return open('game.html').read()

@app.route("/cmd")
def cmd():
    error = None
    cmd = request.args.get('')
    return 'debug', cmd

if __name__ == "__main__":
    app.run(debug = True)
