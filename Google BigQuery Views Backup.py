# Python Script to backup Views from Google BigQuery into .sql file
from datetime import datetime
from google.cloud import bigquery
import os

client = bigquery.Client.from_service_account_json("C:/Users/Public/Documents/service_account.json")

query = f"""
SELECT table_name, view_definition FROM `[PROJECT NAME].[DATASET NAME].INFORMATION_SCHEMA.VIEWS` WHERE LOWER(table_name) LIKE 'vw_%';
"""

query_job = client.query(query)
df = query_job.to_dataframe()

# Get the current date and time
now = datetime.now()

# Format the date and time to a string suitable for a folder name
folder_name = "Views Backup - "+now.strftime("%d-%m-%Y_%H-%M-%S")

# Create the directory in the current working directory
os.makedirs(folder_name, exist_ok=True)

print(f"Created directory: {folder_name}")

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    # Construct the filename using routine_name
    filename = os.path.join(folder_name, f"{row['table_name']}.sql")
    
    # Prepare the content for the .sql file
    content = f"-- backup_time = {now}\n\n{row['view_definition']}"
    
    # Write to the .sql file
    with open(filename, 'w') as file:
        file.write(content)
    
    # print(f"{filename}.sql created successfully!")

print('Backup taken successfully!')
