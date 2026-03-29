import pandas as pd
import sqlite3

# 1. Connect to the SQLite database you just created
conn = sqlite3.connect('/home/wacky/Desktop/netflix_warehouse.db')

# 2. Load your cleaned data
df = pd.read_csv('/home/wacky/Desktop/cleaned_netflix_data.csv')

# 3. Load the data into a temporary staging table
df.to_sql('stg_netflix', conn, if_exists='replace', index=False)

print("Data successfully loaded into the staging table!")
conn.close()
