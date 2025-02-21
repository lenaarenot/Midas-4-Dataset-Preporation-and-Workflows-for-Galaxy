import pandas as pd

# Load the combined Excel file
final_file_path = 'asv_combined_file.xlsx'  
df = pd.read_excel(final_file_path)

# Save the DataFrame to a TSV file
df.to_csv('asv_combined_file.tsv', sep='\t', index=False)

print("File saved as TSV successfully!")
