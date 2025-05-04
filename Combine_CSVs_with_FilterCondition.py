import pandas as pd
import os

# Define the path to the zip file and the output CSV file
files_location = '[FILES_LOCATION]'
output_csv_path = '[OUTPUT_FILE_LOCATION]/combined_filtered_data.csv'

dataframes = []

# Loop through the extracted files
for filename in os.listdir(files_location):
    if filename.startswith("[CONDITION]"):
        file_path = os.path.join(files_location, filename)
        
        # Read the CSV file
        df = pd.read_csv(file_path)

        # Print the columns to check if Skill_Name exists
        print(f"Processing file: {filename}")
        # print(f"Columns in {filename}: {df.columns.tolist()}")
        
        # # Print the first few rows of the DataFrame
        # print(f"First few rows in {filename}:\n{df.head()}")
        
        # Print unique values in the Skill_Name column
        # if 'Skill_Name' in df.columns:
        #     print(f"Unique values in '[FIELD_NAME]' column: {df['[FIELD_NAME]'].unique()}")
        
        df = df.rename(columns={'field1': 'Field1',
                                'field2' : 'Field2'})

        # Rename columns to proper case
        # df.columns = [col.title() for col in df.columns]

        # Filter the DataFrame based on the Skill_Name field
        filtered_df = df[df['[FIELD_NAME]'].str.contains('[CONDITION]', case=False, na=False)]
        
        # Append the filtered DataFrame to the list
        dataframes.append(filtered_df)

# Concatenate all filtered DataFrames into a single DataFrame
combined_df = pd.concat(dataframes, ignore_index=True)

# Duplicated entries
print(f"Duplicated rows count {combined_df.duplicated().sum()}")

# Delete Duplicate entries
combined_df = combined_df.drop_duplicates()

# Save the combined DataFrame to a new CSV file
combined_df.to_csv(output_csv_path, index=False)

print(f"Combined filtered data saved to {output_csv_path}")


# To create separate csv for each year
df_w_year = combined_df.copy()

# Extract year
df_w_year['Year'] = combined_df['Date'].str[-4:]

for year in df_w_year['Year'].unique():
    df_export = df_w_year[df_w_year['Year'] == year]
    df_export.to_csv(f"[LOCATION]/combined_filtered_data_{year}.csv", index=False)
