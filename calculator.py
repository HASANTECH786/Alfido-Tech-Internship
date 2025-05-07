def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

print("Select operation: + - * /")
op = input("Enter operator: ")
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

if op == '+':
    print("Result:", add(x, y))
elif op == '-':
    print("Result:", subtract(x, y))
elif op == '*':
    print("Result:", multiply(x, y))
elif op == '/':
    print("Result:", divide(x, y))
else:
    print("Invalid operator")
