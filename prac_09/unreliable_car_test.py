from unreliable_car import UnreliableCar


def main():
    unreliable_car = UnreliableCar("MaybeCar", 100, 50)  # 50% reliable

    for i in range(1, 11):
        distance_driven = unreliable_car.drive(10)
        print(f"Attempt {i}: drove {distance_driven}km, odometer={unreliable_car.odometer}")


if __name__ == "__main__":
    main()
