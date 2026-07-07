# Q5

# Take three numbers.

# Print the largest number.
# first_number,second_number,third_number = map(int, input("Enter three numbers separated by spaces: ").split())
# largest = max(first_number,second_number,third_number)
# print("The largest number is", largest)

# For interview purpose, we can also use the following code to find the largest number.
# first_number,second_number,third_number = map(int,input("Enter the three numbers with separation by spaces: ").split())

# if first_number >= second_number and first_number >= third_number:
#     print(first_number)

# elif second_number >= first_number and second_number >= third_number:
#     print(second_number)

# else:
#     print(third_number)

# more preciese
first_number,second_number,third_number = map(int,input("Enter the three numbers with separation by spaces: ").split())
if first_number == second_number == third_number:
    print("All numbers are equal")

elif first_number == second_number and first_number > third_number:
    print(f"{first_number} and {second_number} are the largest")

elif first_number == third_number and first_number > second_number:
    print(f"{first_number} and {third_number} are the largest")

elif second_number == third_number and second_number > first_number:
    print(f"{second_number} and {third_number} are the largest")

elif first_number > second_number and first_number > third_number:
    print(f"{first_number} is the largest")

elif second_number > first_number and second_number > third_number:
    print(f"{second_number} is the largest")

else:
    print(f"{third_number} is the largest")