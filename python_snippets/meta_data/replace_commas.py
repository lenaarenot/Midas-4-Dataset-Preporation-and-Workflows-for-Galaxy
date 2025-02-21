import pandas as pd

# Load the TSV file
file_path = 'meta_data_cleaned.tsv'
df = pd.read_csv(file_path, sep='\t')

# Replace commas with underscores in the 'Process_type' column
if 'Process_type' in df.columns:
    df.loc[:, 'Process_type'] = df['Process_type'].str.replace(',', '_', regex=False)  # Replace commas with underscores
    df.loc[:, 'Process_type'] = df['Process_type'].fillna('NA')
    
    # Save the updated DataFrame to altenative file 
    output_file_path = 'meta_data_cleaned_alternative.tsv'
    df.to_csv(output_file_path, sep='\t', index=False)

    # Print confirmation
    print("All commas in the 'Process_type' column have been replaced with underscores.")

    # Print unique values in the 'Process_type' column
    unique_values = set(df['Process_type'].astype(str))
    print("\nUnique values in the 'Process_type' column:")
    print(unique_values)
else:
    print("The column 'Process_type' does not exist in the file.")
