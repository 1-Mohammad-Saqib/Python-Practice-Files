# Q2
# Take marks.

# Print
# Pass
# Fail
# (Passing marks = 40)

# marks = int(input("Enter the marks: "))
# if marks >= 40:
#     print("Pass")
# elif marks < 40:
#     print("Fail")
# elif marks < 0 or marks > 100:
#     print("Invalid value")
# else:
#     print("Invalid value")

# improved code
marks = int(input("Enter the marks: "))
if marks < 0 or marks > 100:
    print("Invalid value")
elif marks >= 40:
    print("Pass")
elif marks < 40:
    print("Fail")
else:
    print("Invalid value")