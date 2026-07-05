# Q5
# Ask for username and password.
correct_username = "saqib"
correct_password = "9210"
username = input("Enter the username: ")
password = input("Enter the password: ")
if username == correct_username:
    if password == correct_password:
        print("You loged in")
    else:
        print("invalid password")
else:
    print("Invalid username")