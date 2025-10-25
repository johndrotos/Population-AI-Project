from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta
import pandas as pd

app = Flask(__name__)
app.secret_key = "Sana"
app.permanent_session_lifetime = timedelta(minutes=5)


population_data = pd.read_csv('data.csv')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        start_year = request.form['start_year']
        end_year = request.form['end_year']
        calculation_result = calculate(start_year, end_year)
        return render_template('index.html', calculation_result=calculation_result)
    else:
        return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate(start_year, end_year):
    # Placeholder for calculation logic
    return f"Calculating population from {start_year} to {end_year}"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form['nm']
        session['user'] = user
        return redirect(url_for('user'))
    else:
        if "user" in session:
            return redirect(url_for('user'))
        return render_template('login.html')

@app.route('/user', methods=['GET', 'POST'])
def user():
    if "user" in session:
        user = session['user']
        return f"<h1>Hello, {user}!</h1>"
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login')) 

if __name__ == '__main__':
    app.run(debug=True)