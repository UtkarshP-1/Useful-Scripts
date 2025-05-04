import pandas as pd
import zipfile
import os

# Define the path to the zip file and the output CSV file
files_location = 'C:/Users/utkarsh.palwekar/Downloads/Contact_Center/'
output_csv_path = 'C:/Users/utkarsh.palwekar/Downloads/combined_filtered_data.csv'

dataframes = []

# Loop through the extracted files
for filename in os.listdir(files_location):
    if filename.startswith("RingCentral"):
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
        #     print(f"Unique values in 'Skill_Name' column: {df['Skill_Name'].unique()}")
        
        df = df.rename(columns={'Contact_Id': 'Contact_ID',
                                'Master_Contact_Id' : 'Master_Contact_ID',
                                'Ani_Dialnum' : 'ANI_DIALNUM',
                                'Start_Time' : 'start_time',
                                'Prequeue' : 'PreQueue',
                                'Inqueue' : 'InQueue',
                                'Agent_Working_Time': 'Agent_Time',
                                'Postqueue' : 'PostQueue',
                                'Total_Time' : 'Total_Time_Plus_Disposition'})

        # Rename columns to proper case
        # df.columns = [col.title() for col in df.columns]

        # Filter the DataFrame based on the Skill_Name field
        filtered_df = df[df['Skill_Name'].str.contains('outbound|OB', case=False, na=False)]
        
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
df_w_year['year'] = combined_df['Start_Date'].str[-4:]

for year in df_w_year['year'].unique():
    df_export = df_w_year[df_w_year['year'] == year]
    df_export.to_csv(f"C:/Users/utkarsh.palwekar/Downloads/Contact_Center_{year}.csv", index=False)
