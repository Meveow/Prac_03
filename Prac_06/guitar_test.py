from guitar_info import GuitarInfo


def main():
    gibson = GuitarInfo("Gibson", 1922, 16035.40)

    print(gibson)
    print(f"Age: {gibson.get_age()}")
    print(f"Vintage: {gibson.is_vintage()}")


main()
