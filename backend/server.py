from flask import Flask
import pandas as pd

app = Flask(__name__)

population_data = pd.read_csv('data.csv')

def estimate_cumulative_births(population_data):
    cumulative_births = 0
    births_by_period = []
    
    for i in range(len(population_data) - 1):
        year1 = population_data.iloc[i]['year']
        year2 = population_data.iloc[i+1]['year']
        pop1 = population_data.iloc[i]['population']
        pop2 = population_data.iloc[i+1]['population']
        
        time_period = year2 - year1
        population_growth = pop2 - pop1
        
        # Rough estimate: assume 30 year life expectancy historically
        # This means ~1/30 of population dies per year
        death_rate = 1/30
        deaths = pop1 * death_rate * time_period
        
        births = population_growth + deaths
        cumulative_births += births
        
    return cumulative_births



@app.route('/home')
def home():
    return {"title": "Population AI Project"}






if __name__ == '__main__':
    app.run(debug=True)