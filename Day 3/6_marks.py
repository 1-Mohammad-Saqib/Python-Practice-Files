# Take marks.

# Print

# A (90+)
# B (75–89)
# C (60–74)
# D (40–59)
# Fail (<40)

marks = int(input("Enter your marks: "))
if marks < 0 or marks > 100:
    print("Invalid value")
elif marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("Fail")