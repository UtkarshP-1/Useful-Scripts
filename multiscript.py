# Python script to generate multiple script where body of script remains same but table name (or any other part) changes
# This will save output in output_script.txt

import os

# Define the array of table names
table_names = ["table1", "table2", "table3", "table4"]  # Add more as needed

# Define the SQL script template with a placeholder
sql_script_template = """
-- {table_name}
SELECT * FROM {table_name} LIMIT 10;
"""

output_file = "output_script.txt"

# Remove the file if it already exists
if os.path.exists(output_file):
    os.remove(output_file)

# Iterate through table names, run the script, and store output
with open(output_file, "a") as file:
    for table_name in table_names:
        # Generate SQL script for the current table
        sql_script = sql_script_template.format(table_name=table_name)
        
        # Simulating execution of the script (replace this part with actual DB execution)
        output_data = f"{sql_script}\n" 
        
        # Append output to text file
        file.write(output_data + "\n")

print(f"Output stored in {output_file}")
