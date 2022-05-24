from silver_service_taxi import SilverService

def main():
    silverservicetaxi = SilverService("White", 100, 2)
    silverservicetaxi.drive(18)
    print(silverservicetaxi)
    print(silverservicetaxi.get_fare())

main()