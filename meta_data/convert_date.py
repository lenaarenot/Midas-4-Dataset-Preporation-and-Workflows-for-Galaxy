import pandas as pd

# Load the data file
file_path = 'meta__data.txt'  
df = pd.read_csv(file_path, sep='\t')

# Convert the date format in the 'Sampling_date' column
# Update 'Sampling_date' to match your date column name exactly
df['Sampling_date'] = pd.to_datetime(df['Sampling_date'], format='%d.%m.%Y', errors='coerce')

# Save as a TSV file
df.to_csv('meta_data.tsv', sep='\t', index=False)

print("Date converted successfully!")
