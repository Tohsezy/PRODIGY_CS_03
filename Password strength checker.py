#password strenth checker
import re

#password must be at least 8 character long
password = input("Enter your password: ")
if len(password) < 8:
    print("Password must be at least 8 characters long.")
#password must contain at least one uppercase letter
elif not re.search("[A-Z]", password):
    print("Password must contain at least one uppercase letter.")
    password = input("Enter your password: ")
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        password = input("Enter your password: ")
#password must contain at least one lowercase letter
elif not re.search("[a-z]", password):
    print("Password must contain at least one lowercase letter.")
    password = input("Enter your password: ")
    if len(password) < 8:
        password = input("Enter your password: ")
#password must contain at least one number
elif not re.search("[0-9]", password):
    print("Password must contain at least one number.")
    password = input("Enter your password: ")
    if len(password) < 8:
        password = input("Enter your password: ")
else:
    print("Password is strong.")