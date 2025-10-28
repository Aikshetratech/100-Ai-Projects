import pandas as pd
from utils import load_data

input_csv = 'data/raw/reviews.csv'
output_csv = 'data/processed/processed_data.csv'

df = load_data(input_csv)
df.to_csv(output_csv, index=False)
print(f"Processed data saved to {output_csv}")
