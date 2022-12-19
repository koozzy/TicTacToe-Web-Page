from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def welcome_page():
    return render_template('index.html')

@app.route("/game")
def game_page():
    return render_template('play.html')

@app.route("/stats")
def game_page():
    return render_template('stats.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)