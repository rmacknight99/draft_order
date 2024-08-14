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
    from teams import data
    managers = data['managers']
    teams = data['teams']
    _teams = [f"{m}: {t}" for m, t in zip(managers, teams)]
    random.shuffle(_teams)
    #store teams to session
    session['order'] = _teams
    return redirect(url_for('order'))

@app.route('/order')
def order():
    teams = session.get('order', [])
    return render_template('order.html', teams=teams)

if __name__ == '__main__':
    app.run(debug=True)