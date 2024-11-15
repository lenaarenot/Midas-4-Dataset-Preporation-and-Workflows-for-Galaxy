import pandas as pd
import os

# Load the Excel file
file_path = "ASV_sorted_columns_part_4.xlsx"  # Replace with the actual file path
df = pd.read_excel(file_path)

print(df.head())

# Combine columns ending in "-A" and "-B"
# Get all unique prefixes (e.g., 'PL-12', 'AR-07', etc.)
prefixes = set(col[:-2] for col in df.columns if col.endswith(('-A', '-B')))

# Loop over each prefix and combine the corresponding '-A' and '-B' columns
for prefix in prefixes:
    col_a = f'{prefix}-A'
    col_b = f'{prefix}-B'
    
    # Check if both columns exist and sum them if both are present
    if col_a in df.columns and col_b in df.columns:
        df[prefix] = df[col_a] + df[col_b]
    elif col_a in df.columns:
        df[prefix] = df[col_a]  # If only -A exists
    elif col_b in df.columns:
        df[prefix] = df[col_b]  # If only -B exists
    
    # Optionally drop the original columns if they exist
    df.drop(columns=[col_a, col_b], errors='ignore', inplace=True)

# Save the result to a new Excel file
output_file_path = "part4.xlsx"
df.to_excel(output_file_path, index=False)
print('combination complete')
