import pandas as pd

# Load the TSV file
file_path = 'meta_data_cleaned_old.tsv'
df = pd.read_csv(file_path, sep='\t')

# Replace NaN values with 'NA' in the 'Process_type' column
if 'Process_type' in df.columns:
    df.loc[:, 'Process_type'] = df['Process_type'].fillna('NA')  # Explicitly assign back to the column

    # Save the updated DataFrame back to a file (optional)
    output_file_path = 'meta_data_cleaned.tsv'
    df.to_csv(output_file_path, sep='\t', index=False)

    # Print confirmation
    print("All NaN values in the 'Process_type' column have been replaced with 'NA'.")
    unique_values = set(df['Process_type'].astype(str))
    print("\nUnique values in the 'Process_type' column:")
    print(unique_values)
else:
    print("The column 'Process_type' does not exist in the file.")
