a = input("Enter the number of Fibonacci terms to generate: ")
a = int(a)

def Fibonacci(a):
    fib = [0, 1]
    for i in range(1, a - 1):
        fib.append(fib[i-1] + fib[i])
    yield fib
print(*Fibonacci(a))
    