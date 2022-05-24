from taxi import Taxi
from silver_service_taxi import SilverService


def main():
    print("Let's drive!")
    menu = "q)uit, c)hoose taxi, d)rive"
    print(menu)
    taxis = [Taxi("Prius", 100), SilverService("Limo", 100, 2), SilverService("Hummer", 200, 4)]
    bill = 0
    current_taxi = None
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid choice")
        elif choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                distance = float(input("Drive how far? "))
                current_taxi.drive(distance)
                cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${cost:.2f}")
                bill += cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill}")
        print(menu)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now: ")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")  # display number of taxis, and details


main()
