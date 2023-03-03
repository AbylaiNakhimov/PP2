import os

path = input("Enter the path: ")
file_type = input("Enter the file type (e.g. 'py'): ")
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith("." + file_type):
            print(os.path.join(root, file))