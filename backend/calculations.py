import pandas as pd
import os



def do_calculation(start_year, end_year, data):
    starting_population = data.loc[data['Year'] == start_year, 'Population'].values[0]
    total_births = data.loc[(data['Year'] == end_year), 'Cumulative_Births'].values[0] - (
                        data.loc[(data['Year'] == start_year), 'Cumulative_Births'].values[0]
                    )
    people_alive = starting_population + total_births
    total_people = data.loc[data['Year'] == 2025, 'Cumulative_Births'].values[0]
    percent = (people_alive / total_people) * 100
    percent = round(percent, 2)
    return percent

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, 'data1.csv')
    data = pd.read_csv(csv_path)

    start_year = 1950
    end_year = 2025
    result = do_calculation(start_year, end_year, data)
    print(f"Percentage of people born between {start_year} and {end_year}: {result}%")