"""Check length of password"""
MIN_LENGTH = 5
symbol = "*"


def main():
    get_password()


def get_password():
    password = input("Password: ")
    while len(password) < MIN_LENGTH:
        print("Must meet minimum length of 5")
        password = input("Password: ")
    print_asterisks(password)


def print_asterisks(password):
    print(symbol * len(password))


main()
