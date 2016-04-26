from flask import Flask
from flask import request
from flask import render_template
import engine

#engine.io(cmd) sends cmd to engine

app = Flask(__name__)

@app.route("/")
def menu():
    return open('static/menu.html').read()

@app.route("/game")
def game():
    return open('static/game.html').read()

@app.route("/cmd")
def cmd():
    cmd = request.args.get('')
    engine.io(cmd)
    return 'debug'


if __name__ == "__main__":
    app.run(debug = True)
