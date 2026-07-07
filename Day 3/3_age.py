# Q3
# Take age.
# Print whether the user can vote.
age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote")
elif age < 18 and age > 0:
    print("You can not vote")
else :
    print("Invalid value")