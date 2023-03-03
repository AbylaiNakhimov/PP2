filename = input("Enter name of text file: ")
word = input("Enter a word to find: ")
with open(filename, "r") as file:
    text = file.read()
    count = text.count(word)
    
print(f"The word '{word}' occurs {count} times.")