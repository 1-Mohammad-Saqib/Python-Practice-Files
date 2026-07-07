# Q4
# Take a number.
# Check whether it is
# Even
# Odd
# while True:
#     number = int(input("Enter a number: "))
#     if number <= 0 :
#         print("Enter the positive integer only")
#     elif number % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")

#     choice = input("Do you want to continue or exit : ")
#     if choice == 'continue':
#         pass
#     elif choice == 'exit':
#         print("Thanks for using my programme")
#         break
#     else:
#         print("Invalid input")
        
# improved code
while True:
    number = int(input("Enter a number: "))
    if number <= 0 :
        print("Enter the positive integer only")
    elif number % 2 == 0:
        print("Even")
    else:
        print("Odd")

    choice = input("Do you want to continue or exit : ")
    if choice == 'continue':
        continue
    elif choice == 'exit':
        print("Thanks for using my programme")
        break
    else:
        print("Invalid input")
