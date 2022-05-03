from guitar_info import GuitarInfo


def main():

    guitars = []
    print("My guitars!")
    name = ''
    while name != " ":
        name = input("Name: ")
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        print(f"{name} ({year}) : ${cost} added.")
        guitars.append([name, year, cost])
    else:
        print("... snip ...")

    guitars.append(Guitar())
    print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                              guitar.is_vintage))

    # gibson = GuitarInfo("Gibson", 1922, 16035.40)
    #
    # print(gibson)
    # print(f"Age: {gibson.get_age()}")
    # print(f"Vintage: {gibson.is_vintage()}")


main()
