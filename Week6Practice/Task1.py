import re 
a = input("Enter a sentence with word Python:  ")
b = re.sub("Python", "Java", a)
print(b)