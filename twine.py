from flask import Flask
from flask import request
from engine import io


app = Flask(__name__)

@app.route("/")
def menu():
    return open('menu.html').read()

@app.route("/game")
def game():
    return open('game.html').read()

@app.route("/cmd")
def cmd():
    try:
        cmd = request.args.get('')
        return cmd
    except ValueError:
        return 'Unknown command'


if __name__ == "__main__":
    app.run(debug = True)
