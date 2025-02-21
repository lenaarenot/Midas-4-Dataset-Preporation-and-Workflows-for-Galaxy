import pandas as pd

# Load the data file
file_path = 'meta_data2.tsv'  
df = pd.read_csv(file_path, sep='\t')

# Convert 'Sampling_date' to datetime format if it is not already
df['Sampling_date'] = pd.to_datetime(df['Sampling_date'], errors='coerce').dt.strftime('%Y-%m-%d')

# Identify rows with unparsed dates
invalid_dates = df[df['Sampling_date'].isnull()]

"""
# Print a warning if any dates couldn't be parsed
if not invalid_dates.empty:
    print("Warning: Some dates couldn't be parsed correctly. Please check the following rows:")
    print(invalid_dates)
"""
# Drop rows with unparsed dates 
df = df.dropna(subset=['Sampling_date'])

# Save as a TSV file
df.to_csv('meta_data_cleaned.tsv', sep='\t', index=False)

print("File saved with correctly formatted dates in 'Sampling_date' column.")
