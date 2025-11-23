from random import randint
from car import Car


class UnreliableCar(Car):
    """Car that sometimes doesn't drive when you tell it to."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar with reliability percentage."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """
        Attempt to drive the car.
        Only drive if random number < reliability.
        Always return distance actually driven (0 or positive).
        """
        random_number = randint(0, 100)
        if random_number < self.reliability:
            return super().drive(distance)
        return 0
