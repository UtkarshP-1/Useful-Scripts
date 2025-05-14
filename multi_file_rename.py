# Python program to rename multiple files with different name using dictionary for name mapping keeping extension intact 

import os 

filenames = {
    "Old Filename 1" : "New Filename 1",
    "Old Filename 2" : "New Filename 2"
}

os.chdir("[FILE LOCATION]")

# print(os.getcwd()) # to check current working directory has changed to file location provided in prev step


for file in os.listdir():                                                            # iterate through files in directory
    for key, value in filenames.items():                                             # iterate through filenames dictionary
        if file.startswith(key):                                                     # matches filename in filenames dictionary to rename 
            os.rename(file, value + '.' + file.split('.') [1])                       # renames file keeping extension same as old file 
            print(f"File {file} renamed to {value + '.' + file.split('.') [1]}")     # prints successfully renamed message
