from flask import Flask
import pandas as pd

app = Flask(__name__)

population_data = pd.read_csv('data.csv')


@app.route('/home')
def home():
    return {"title": "Population AI Project"}






if __name__ == '__main__':
    app.run(debug=True)