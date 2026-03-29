import pandas as pd

# 1. Load the data using the path we verified works
df = pd.read_csv('/home/wacky/Desktop/netflix_titles.csv')

print("Starting Transformation...")

# 2. Handle missing values (The 'T' in ETL)
# We fill 'Unknown' so the database doesn't have empty (NULL) values
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')

# 3. Data Cleaning
# Drop rows where 'rating' is missing since there are only 4 of them
df.dropna(subset=['rating'], inplace=True)

# 4. Save the "Cleaned" version to your Desktop
# This cleaned file is what we will 'Load' into the Data Warehouse
output_path = '/home/wacky/Desktop/cleaned_netflix_data.csv'
df.to_csv(output_path, index=False)

print(f"Success! Cleaned data saved to: {output_path}")
print(f"Rows processed: {len(df)}")
