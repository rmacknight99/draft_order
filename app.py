from flask import Flask, render_template, redirect, url_for
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate')
def generate():
    with open('teams.txt', 'r') as f:
        teams = [line.strip() for line in f.readlines()]
    random.shuffle(teams)
    return render_template('order.html', teams=teams)

if __name__ == '__main__':
    app.run(debug=True)
