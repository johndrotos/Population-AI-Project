import os
import pandas as pd
 

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'data1.csv')

data1 = pd.read_csv(csv_path)
data1 = data1.round(1)
data1.to_csv('data1.csv', index=False)