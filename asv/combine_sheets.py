import pandas as pd
import os

# List the file paths for all the split Excel files
file_paths = ['part1.xlsx', 'part2.xlsx', 'part3.xlsx', 'part4.xlsx']  # Add splited file paths

# Initialize an empty list to hold DataFrames
dfs = []

# Load each file into a DataFrame and append to list
for file_path in file_paths:
    df = pd.read_excel(file_path)
    dfs.append(df)

# Concatenate all DataFrames, ensuring to align them by the 'ASV' column
combined_df = pd.concat(dfs, axis=1)

# Remove duplicate 'ASV' columns if they exist
combined_df = combined_df.loc[:,~combined_df.columns.duplicated()]

# Save the combined file
combined_df.to_excel('asv_combined_file.xlsx', index=False)

print("Files combined successfully!")
