# Python Script to backup Google BigQuery Routines to SQL files with last altered datetime as header
# This script will create a folder with date and timestamp as name in the location where this python file is located

from datetime import datetime
from google.cloud import bigquery
import os

# Get the current date and time
now = datetime.now()

# Format the date and time to a string suitable for a folder name
folder_name = os.getcwd()+r'\\Routine Backup\\'+now.strftime("%d-%m-%Y_%H-%M-%S")

# Create the directory in the current working directory
os.makedirs(folder_name, exist_ok=True)

print(f"Created directory: {folder_name}")

client = bigquery.Client.from_service_account_json("C:/Users/Public/Documents/service_account.json")

# Routines with 'test' and 'bkp' in name will be excluded. There were too many in case hence added it. 
query = f"""
SELECT routine_name, ddl, DATETIME(last_altered,"Asia/Kolkata")AS last_altered
FROM `[PROJECT NAME].[DATASET NAME].INFORMATION_SCHEMA.ROUTINES`
WHERE lower(routine_name) NOT LIKE '%test%' AND lower(routine_name) NOT LIKE '%bkp%' ;
"""

query_job = client.query(query)
df = query_job.to_dataframe()

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    # Construct the filename using routine_name
    filename = os.path.join(folder_name, f"{row['routine_name']}.sql")
    
    # Prepare the content for the .sql file
    content = f"last_altered_time = {row['last_altered']}\n\n{row['ddl']}"
    
    # Write to the .sql file
    with open(filename, 'w') as file:
        file.write(content)
    
    # print(f"{filename}.sql created successfully!")

# print(df.head())

print(f'Routines backedup successfully!')
