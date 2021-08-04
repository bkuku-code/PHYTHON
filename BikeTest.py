import unittest

from Bike import Bike
from Bike_Exception import EmptyFuelException


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.bike1 = Bike("product_name", 0, 3)

    def test_something(self):
        self.assertEqual(True, True)

    def test_Bike_can_on(self):
        self.assertFalse(self.bike1.on)

        self.bike1.power()
        self.assertTrue(self.bike1.on)
        self.assertIsInstance(self.bike1.on, bool)

    def test_Bike_Speed(self):
        self.assertIsNotNone(self.bike1.speed)
        self.assertIsNotNone(self.bike1.speed, str)

    def test_Bike_can_off(self):
        self.assertFalse(self.bike1.on)

        self.bike1.power()
        self.assertTrue(self.bike1.on)

        self.bike1.power()
        self.assertFalse(self.bike1.on)

    def test_Bike_product_name(self):
        self.assertIsNotNone(self.bike1.product_name)
        self.assertIsInstance(self.bike1.product_name, str)

    def test_for_fuel(self):
        self.assertIsNotNone(self.bike1.fuel)
        self.assertIsInstance(self.bike1.fuel, int)

    def test_that_speed_raises_error_when_fuel_is_empty(self):
        self.assertEqual(3, self.bike1.fuel)
        self.bike1.fuel = 0
        self.assertRaises(EmptyFuelException, self.bike1.speeding)


if __name__ == '__main__':
    unittest.main()
