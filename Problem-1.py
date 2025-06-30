a = int(input("value1: "))
b = int(input("value2: "))
ope = input("Operation (+, -, *, /): ")

if ope == "+":
    print(a + b)
elif ope == "-":
    print(a - b)
elif ope == "*":
    print(a * b)
elif ope == "/":
    if b == 0:
        print("Cannot divide by zero")
    else:
        print(a / b)
else:
    print("Invalid operator")