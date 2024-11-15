import pandas as pd

# Load the data file
file_path = 'tax_complete.csv'
df = pd.read_csv(file_path)

# Clean the first column: replace 'FLASV' with 'ASV' and remove the dot and numbers after it
df[df.columns[0]] = df[df.columns[0]].str.replace(r'^FLASV(\d+)\.\d+$', r'ASV\1', regex=True)

# Save as a TSV file
df.to_csv('tax_complete_asv.tsv', index=False)

print("First column cleaned up and file saved successfully!")
