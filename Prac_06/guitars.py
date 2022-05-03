from guitar_info import GuitarInfo


def main():
    guitars = []

    print("My guitars!")
    # name = input("Name: ")
    # while name != "":
    #     year = int(input("Year: "))
    #     cost = float(input("Cost: $"))
    #     add_guitar = GuitarInfo(name, year, cost)
    #     guitars.append(add_guitar)
    #     print(f"{name} ({year}) : ${cost} added.")
    #     name = input("Name: ")

    guitars.append(GuitarInfo("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(GuitarInfo("Line 6 JTV-59", 2010, 1512.9))

    print("\n...snip...\n")

    print("These are my guitars:")
    count = 0
    for i, guitar in enumerate(guitars, 1):
        count += 1
        vintage = ""
        if guitar.is_vintage():
            vintage = "(vintage)"
        print(f"Guitar {count}: {guitar.name:>20} ({guitar.year}), worth $ {guitar.cost:10,.2f} {vintage}")


main()
