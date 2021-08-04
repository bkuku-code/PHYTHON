from ACException import temperatureError, NoOnException


class Ac:

    def __init__(self, temperature: int, product_name: str):
        self.on = False
        self.temperature = temperature
        self.product_name = product_name
        self.temperature = 16
        self.max_temperature = 35

    def power(self):
        self.on = not self.on

    def temp(self):
        if self.temperature < 16:
            raise temperatureError()

        if not self.on:
            raise NoOnException()

    def increase_temp(self):
        if self.on:
            if self.temperature > 16:
                self.temperature = self.temperature - 1

    def decrease_temp(self):
        if self.on:
            if self.temperature < self.max_temperature:
                self.temperature = self.temperature + 1
