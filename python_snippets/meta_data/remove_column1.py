import pandas as pd

# Load the .txt file (assuming it's tab-separated)
file_path = 'meta__data_alt.txt'  
df = pd.read_csv(file_path, sep='\t')

# Drop the first column
df.drop(df.columns[0], axis=1, inplace=True)

# Save the result back to a new .txt file 
df.to_csv('meta__data.txt', sep='\t', index=False)

print("First column removed and file saved successfully!")
