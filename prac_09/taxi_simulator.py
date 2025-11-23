from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi simulator program."""
    print("Let's drive!")
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4),
    ]
    bill_to_date = 0.0
    current_taxi = None

    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                bill_to_date += drive_taxi(current_taxi)
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def choose_taxi(taxis):
    """Display taxis and return chosen taxi, or None if invalid."""
    print("Taxis available:")
    display_taxis(taxis)
    try:
        taxi_choice = int(input("Choose taxi: "))
        chosen_taxi = taxis[taxi_choice]
        return chosen_taxi
    except (ValueError, IndexError):
        print("Invalid taxi choice")
        return None


def drive_taxi(taxi):
    """Start a new fare, drive, and return trip cost."""
    taxi.start_fare()
    try:
        distance = float(input("Drive how far? "))
    except ValueError:
        print("Invalid distance")
        return 0.0
    taxi.drive(distance)
    trip_cost = taxi.get_fare()
    print(f"Your {taxi.name} trip cost you ${trip_cost:.2f}")
    return trip_cost


def display_taxis(taxis):
    """Print all taxis with index."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
