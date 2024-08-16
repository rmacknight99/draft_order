from flask import Flask, render_template, session, redirect, url_for
import secrets, random, pytz, datetime
from teams import data

def _shuffle(data):
    managers = data['managers']
    teams = data['teams']
    _teams = [f"{m}: {t}" for m, t in zip(managers, teams)]
    # Get order of indices
    indices = list(range(len(_teams)))
    random.shuffle(indices)
    managers = [managers[i] for i in indices]
    teams = [teams[i] for i in indices]
    return [(i, m, t) for i, m, t in zip(range(1, len(_teams) + 1), managers, teams)]

def get_formatted_time():
    # Define the timezone
    est = pytz.timezone('US/Eastern')

    # Get the current time in UTC and then convert to Eastern time
    now_utc = datetime.datetime.now(pytz.utc)
    now_est = now_utc.astimezone(est)

    # Define ordinal suffixes
    def get_ordinal_suffix(n):
        if 11 <= (n % 100) <= 13:
            return 'th'
        else:
            return {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')

    # Extract parts of the date and time
    day = now_est.day
    month = now_est.strftime('%B')
    year = now_est.year
    time = now_est.strftime('%I:%M:%S %p')

    # Format the date with the ordinal suffix and time with timezone
    date_with_suffix = f"{month} {day}{get_ordinal_suffix(day)} {year}"
    formatted_date_time = f"{date_with_suffix}, {time} Eastern"

    return formatted_date_time

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_order', methods=['POST'])
def generate_order():
    order = _shuffle(data)
    #store teams to session
    session['order'] = order
    print(order)
    session['formatted_time'] = get_formatted_time()
    print(session['formatted_time'])
    return redirect(url_for('order'))

@app.route('/order')
def order():
    order = session.get('order', [])
    current_time = session.get('formatted_time', None)
    return render_template('order.html', current_time=current_time, order=order)

if __name__ == '__main__':
    app.run(debug=True)