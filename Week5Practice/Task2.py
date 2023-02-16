from module import *

x = float(input("First: "))
y = float(input("Second: "))
operation = input("Select the method(+, -, *, /): ")

if operation == '+':
    result = add(x, y)
    print("Result:", result)
elif operation == '-':
    result = subtract(x, y)
    print("Result:", result)
elif operation == '*':
    result = multiply(x, y)
    print("Result:", result)
elif operation == '/':
    result = divide(x, y)
    print("Result:", result)
else:
    print("Invalid operation")
