from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised Taxi that includes flagfall and fanciness multiplier."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise SilverServiceTaxi with fanciness."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        # Create an instance-level price_per_km based on the class-level Taxi price
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return fare including flagfall, rounded to nearest 10 cents via Taxi.get_fare."""
        return self.flagfall + super().get_fare()

    def __str__(self):
        """Return string with flagfall shown."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
