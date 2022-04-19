def main():
    email_to_name = {}
    email_address = input("Email: ")
    while email_address != '':
        name = names(email_address)


    for email_address, name in email_to_name.items():
        print(f"{name:13}, {email_address}")


def names(email_address):
    splitting = email_address.split('@')[0]
    name = splitting.split('.')[0].title()
    return name


main()
