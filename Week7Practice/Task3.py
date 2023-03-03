file = input("Enter file name: ")
with open(file, 'w') as f:
    line = input("Enter a line of text: ")

    while line:
        f.write(line + '\n')
        line = input("Enter another line of text (or an empty line to finish): ")
        
with open(file, 'r') as f:
    contents = f.read()
    print("The contents of the file:")
    print(contents)