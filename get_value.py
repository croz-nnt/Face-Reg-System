import pandas as pd


database_path = 'app/database/database.csv'

data = pd.read_csv(database_path)
id = 0
print(data.loc[id]['name'])