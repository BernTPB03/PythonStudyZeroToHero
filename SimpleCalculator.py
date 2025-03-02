def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b if b != 0 else "Error: Division by zero"

op = input("Choose operation (+, -, *, /): ")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

operations = {'+': add, '-': sub, '*': mul, '/': div}
print("Result:", operations[op](a, b) if op in operations else "Invalid operation")
