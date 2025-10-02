password = "admin"

pwd = input("Enter the password:")

while pwd != password:
    print("Incorrect password, try again.")
    pwd = input("Enter the password:")
print("Access granted.")
