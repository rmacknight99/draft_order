from flask import Flask, render_template, session, redirect, url_for
import secrets
import json
import random

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_order', methods=['POST'])
def generate_order():
    with open('teams.json', 'r') as f:
        teams = json.load(f)['teams']
    random.shuffle(teams)
    #store teams to session
    session['teams'] = teams
    return redirect(url_for('order'))

@app.route('/order')
def order():
    teams = session.get('teams', [])
    return render_template('order.html', teams=teams)

if __name__ == '__main__':
    app.run(debug=True)