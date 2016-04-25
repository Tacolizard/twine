from flask import Flask
app = Flask(__name__)

@app.route("/")
def menu():
    return open('menu.html').read()

@app.route("/game")
def game():
    return open('game.html').read()

if __name__ == "__main__":
    app.run(debug = True)
