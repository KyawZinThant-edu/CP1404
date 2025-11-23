from silver_service_taxi import SilverServiceTaxi


def main():
    hummer = SilverServiceTaxi("Hummer", 200, 2)
    hummer.drive(18)
    fare = hummer.get_fare()
    print(hummer)
    print(f"Fare for 18km: ${fare:.2f}")

    # Assert approx equals 48.8 (rounding to 10c)
    assert abs(fare - 48.8) < 0.01, f"Fare was {fare}, expected about 48.8"



main()
