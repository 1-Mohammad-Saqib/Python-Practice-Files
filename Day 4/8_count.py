# Q8
# Count how many even and odd numbers exist between 1 and 100.
even_count = 0
odd_count = 0
for i in range(1,101):
    if i % 2 == 0:
        even_count += 1
    elif i % 2 != 0:
        odd_count += 1
print(f"The count of even number is {even_count} and odd number is {odd_count}")