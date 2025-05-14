import os 

filenames = {
    "Old Filename 1" : "New Filename 1",
    "Old Filename 2" : "New Filename 2"
}

os.chdir("[FILE LOCATION]")

# print(os.getcwd()) 

# print(os.listdir())

# print(filename)

for file in os.listdir():
    for key, value in filenames.items():
        if file.startswith(key):
            # ext = file.split('.') [1]
            # print(ext)
            # print(file, value)
            os.rename(file, value + '.' + file.split('.') [1])
            print(f"File {file} renamed to {value + '.' + file.split('.') [1]}")
