print("Create Account.")
name = input("Enter your username: ")
password = input("Enter your password: ")
confirm = ''
while confirm != password:
    confirm = input("Confirm Password: ")
    if confirm != password:
        print("Passwords do not match")
    else:
        print("Account Created")

print("Login")
user_name = input("Enter your username: ")
user_pass = input("Enter password: ")
if user_name != name:
    print("Username does not match")
elif user_pass != password:
    print("Password does not match")
else:
    print("Login successful")