# Python Script to extract data from Google BigQuery and dump into csv file using service account json file
import time
import datetime
from google.cloud import bigquery
import os

# to get elapsed time of whole process
start_time = time.time()

client = bigquery.Client.from_service_account_json("[SERVICE ACCOUNT JSON LOCATION]")

def extract_file(field_name):
    extarction_started = time.time()  # to get elapsed time of single file/function call

    query = f"""
    SELECT
      *
    FROM
      [PROJECT NAME].[DATASET NAME].[TABLE NAME]
    WHERE
      [FIELD NAME] = [VALUE N]
      AND [OTHER CONDITION/S];
    """

    query_job = client.query(query)
    df = query_job.to_dataframe()

    # To change certain field's format from string to other datatype. I am changing to float here
    cols_to_format = ['[FIELD 1]', '[FIELD 2]','[FIELD 3]']

    for col in cols_to_format:
        df[col] = df[col].apply(lambda x: f"{x:.2f}")

    # create and save data in csv with certain field's name
    df.to_csv(f"C:/Users/Public/Desktop/{field_name}_file.csv",index=False,float_format="%.2f")

    extarction_ended = time.time()

    print(f"Successfully created {field_name}_file.csv file in {str(datetime.timedelta(seconds=extarction_ended-extarction_started))} sec")

field_names = ['[VALUE 1]','[VALUE 2]','[VALUE 3]'] 

for field_name in field_names:
    extract_file(field_name)

# to rename a particular file differently
try:
    os.rename("C:/Users/Public/Desktop/dbu/CDDA-CEC_DBUfile.csv","C:/Users/Public/Desktop/dbu/[EXISTING FILENAME].csv")
except:
    os.remove("C:/Users/Public/Desktop/dbu/[NEW FILENAME].csv")
    os.rename("C:/Users/Public/Desktop/dbu/[EXISTING FILENAME].csv","C:/Users/Public/Desktop/dbu/[NEW FILENAME].csv")

end_time = time.time()

print(f"Success!\nCode execution time : {str(datetime.timedelta(seconds=end_time-start_time))}")
