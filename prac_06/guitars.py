from guitar import Guitar

def main():
    print("My guitars!")
    guitars = []

    name = input("Name: ").strip()
    while name:
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ").strip()

    if guitars:
        print("\nThese are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_tag = " (vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}:{guitar.name:>20} ({guitar.year}), "
                  f"worth ${guitar.cost:10,.2f}{vintage_tag}")
    else:
        print("No guitars.")

main()
