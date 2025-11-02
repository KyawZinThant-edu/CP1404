from guitar import Guitar
from datetime import date

def main():
    l5 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another = Guitar("Another Guitar", 2013, 0)

    current_year = date.today().year
    print(f"{l5.name} get_age() - Expected {current_year-1922}. Got {l5.get_age()}")
    print(f"{another.name} get_age() - Expected {current_year-2013}. Got {another.get_age()}")

    print(f"{l5.name} is_vintage() - Expected True. Got {l5.is_vintage()}")
    print(f"{another.name} is_vintage() - Expected False. Got {another.is_vintage()}")

main()
