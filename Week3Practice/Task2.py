def calculator(operation, num1, num2):    
  operations = {
        '+': lambda x, y: x + y,        
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,        
        '/': lambda x, y: x / y
    }    
  return operations[operation](num1, num2)
for i in range(1):    
    a = int(input())
    b = int(input())    
    c = input("Choose the operation to calculate (add,subtract, multiply, divide):")
    if c == 'add':        
      print(calculator('+', a, b))
    elif c == 'subtract':        
      print(calculator('-', a, b))
    elif c == 'multiply':        
      print(calculator('*', a, b))
    elif c == 'divide':         
      print(calculator('/', a, b))