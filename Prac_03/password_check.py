MIN_LENGTH = 5
symbol = "*"


password = input("Password: ")
while len(password) < MIN_LENGTH:
    print("Must meet the minimum length")
    password = input("Password: ")
else:
    print(symbol*len(password))
