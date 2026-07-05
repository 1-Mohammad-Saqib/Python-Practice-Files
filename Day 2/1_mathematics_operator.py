# Q1
# Take two numbers and print:
# Addition
# Subtraction
# Multiplication
# Division
# Floor Division
# Modulus
# Power

a = int(input("Enter the first number: "))
o = input("Enter the operator: + , - , * , / , // , % , ** :")
c = int(input("Enter the second number: "))
if o == '+':
    print(f"The result of {a} {o} {c} is :", a + c)

elif o == '-':
    print(f"The result of {a} {o} {c} is :", a - c)

elif o == '*':
    print(f"The result of {a} {o} {c} is :", a * c)

elif o == '/':
    print(f"The result of {a} {o} {c} is :", a / c)

elif o == '//':
    print(f"The result of {a} {o} {c} is :", a // c)

elif o == '%':
    print(f"The result of {a} {o} {c} is :", a % c)

elif o == '**':
    print(f"The result of {a} {o} {c} is :", a ** c)
