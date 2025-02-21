import pandas as pd

# Load the dataset
file_path = "ASV_sort.xlsx"  
df = pd.read_excel(file_path)

# Identify the first column (ASVs)
first_column = df.iloc[:, 0]  # This is the first column

# Identify the columns with suffixes '-A' and '-B' (excluding the first column)
columns = df.columns[1:]  # Skip the first column
prefixes = set(col[:-2] for col in columns if col.endswith(('-A', '-B')))

# Number of parts to split into
num_parts = 4  # Number of sheets 

# Calculate the number of prefixes per part
prefixes_per_part = len(prefixes) // num_parts

for i in range(num_parts):
    start = i * prefixes_per_part
    if i == num_parts - 1:  # Last part gets all remaining prefixes
        end = len(prefixes)
    else:
        end = (i + 1) * prefixes_per_part
    
    part_prefixes = list(prefixes)[start:end]
    
    # Collect columns for the current part
    part_columns = [f'{prefix}-A' for prefix in part_prefixes if f'{prefix}-A' in columns] + \
                   [f'{prefix}-B' for prefix in part_prefixes if f'{prefix}-B' in columns]
    
    # Create a DataFrame with the first column and the selected columns
    part_df = pd.concat([first_column, df[part_columns]], axis=1)
    
    # Save the current part to an Excel file
    output_file = f"ASV_sorted_columns_part_{i+1}.xlsx"
    part_df.to_excel(output_file, index=False)
    
    print(f"Saved {output_file} with prefixes from {part_prefixes[0]} to {part_prefixes[-1]}")

print("Column splitting completed.")
