from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Luxury taxi class, inheriting from Taxi, adding a luxury coefficient and a starting fee"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialize the luxury taxi"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        # Price per kilometer = Base price × Luxury coefficient
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Calculate the total cost: basic fee + initial fee"""
        base_fare = super().get_fare()
        return base_fare + self.flagfall

    def __str__(self):
        """Return the string of luxury taxi"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"