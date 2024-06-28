import pandas as pd

# Path to the original reviews.csv file
input_csv = 'Reviews.csv'

# Path to the new limited CSV file
output_csv = 'reviews_limited.csv'

# Number of rows to limit to
limit_rows = 1500

# Read the original CSV file
df = pd.read_csv(input_csv)

# Limit to the first 1500 rows
df_limited = df.head(limit_rows)

# Write the limited DataFrame to a new CSV file
df_limited.to_csv(output_csv, index=False)

print(f"Successfully created {output_csv} with {limit_rows} rows.")
