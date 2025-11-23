from car import Car


class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""
    price_per_km = 1.23

    def __init__(self, name, fuel):
        """Initialise a Taxi with name, fuel and fare-related attributes."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def __str__(self):
        """Return string like: Prius, fuel=100, odometer=0, 0km on current fare, $1.23/km"""
        return f"{super().__str__()}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km"

    def get_fare(self):
        """Return the price for the taxi trip, rounded to nearest 10 cents."""
        fare = self.price_per_km * self.current_fare_distance
        return round(fare, 1)  # round to 10c

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """
        Drive like Car, but also accumulate fare distance.
        Return the distance actually driven.
        """
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven
