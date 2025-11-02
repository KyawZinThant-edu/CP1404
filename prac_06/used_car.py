"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""
from car import Car


def main():
    """Demo test code to show how to use the Car class."""
    # 1. Existing car
    my_car = Car("My car", 180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    # 2. Limo test (new car)
    limo = Car("Limo", 100)   # Create new car with 100 fuel
    limo.add_fuel(20)         # Add 20 more
    print(f"Limo has fuel: {limo.fuel}")  # Print amount of fuel
    limo.drive(115)           # Try to drive 115 km
    print(limo)               # Print to see final fuel and odometer


main()
