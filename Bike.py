import self

from Bike_Exception import EmptyFuelException, NoOnException


class Bike:

    def __init__(self, product_name: str, fuel: int):
        self.on = False
        self.speed = 0
        self.product_name = product_name
        self.fuel = fuel
        self.max_speed: int = 30

    def power(self):
        self.on = not self.on

    def speeding(self):
        if self.fuel <= 0:
            raise EmptyFuelException()
        if not self.on:
            raise NoOnException()
        self.increase_speed()

    def increase_speed(self):
        if self.on:
            if self.speed < self.max_speed:
                self.speed = self.speed + 1

    def decrease_speed(self):
        if self.on:
            if self.speed > 0:
                self.speed = self.speed - 1
