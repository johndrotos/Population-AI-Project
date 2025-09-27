import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'data.csv')

population_data = pd.read_csv(csv_path, sep='\t')

def estimate_cumulative_births(population_data):
    cumulative_births = 0
    
    for i in range(len(population_data) - 1):
        year1 = population_data.iloc[i]['Year']
        year2 = population_data.iloc[i+1]['Year']
        pop1 = population_data.iloc[i]['Population']
        pop2 = population_data.iloc[i+1]['Population']
        
        time_period = year2 - year1
        
        # Use crude birth rate instead
        # Historically ~40-50 births per 1000 people per year
        birth_rate = 0.045  # 45 per 1000
        
        # Average population during the period
        avg_pop = (pop1 + pop2) / 2
        
        births = avg_pop * birth_rate * time_period
        cumulative_births += births
    print(f"Cumulative Births Estimate: {cumulative_births}")
    return cumulative_births


if __name__ == "__main__":
    estimate_cumulative_births(population_data)