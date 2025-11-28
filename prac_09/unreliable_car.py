from car import Car
import random


class UnreliableCar(Car):
    """A derived class of the Car class, whose driving status depends on a random probability."""
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempting to travel a specified distance; success depends on reliability."""
        random_car = random.uniform(1,100)
        if random_car < self.reliability:
            return super().drive(distance)
        else:
            return 0

