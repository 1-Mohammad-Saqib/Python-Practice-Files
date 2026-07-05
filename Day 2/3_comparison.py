# Q3
# Take two numbers and print the results of all comparison operators.
a = int(input("Enter The first number: "))
o = input("Enter the comparision operator: = , != , < , > , <= or >= : ")
b = int(input("Enter the second number: "))

if o == '=':
    print("The result of {a} {o} {b} is :", a is b)

elif o == '!=':
    print("The result of {a} {o} {b} is :", a != b)

elif o == '<':
    print("The result of {a} {o} {b} is :", a < b)

elif o == '>':
    print("The result of {a} {o} {b} is :", a > b)

elif o == '<=':
    print("The result of {a} {o} {b} is :", a <= b)

elif o == '>=':
    print("The result of {a} {o} {b} is :", a >= b)