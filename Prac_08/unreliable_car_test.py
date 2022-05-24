from unreliable_car import UnreliableCar


def main():
    unreliable_car1 = UnreliableCar("Tayoto", 100, 70)
    unreliable_car2 = UnreliableCar("Hunda", 100, 30)
    unreliable_car1.drive(50)
    print(unreliable_car1)
    unreliable_car2.drive(50)
    print(unreliable_car2)


main()
