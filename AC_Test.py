import unittest

from AC import Ac
from ACException import NoOnException


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.ac = Ac(16, "product_name")

    def test_something(self):
        self.assertEqual(True, True)

    def test_Ac_can_on(self):
        self.assertFalse(self.ac.on)

        self.ac.power()
        self.assertTrue(self.ac.on)
        self.assertIsInstance(self.ac.on, bool)

    def test_Ac_can_off(self):
        self.assertFalse(self.ac.on)

        self.ac.power()
        self.assertTrue(self.ac.on)
        self.assertIsInstance(self.ac.on, bool)

    def test_Ac_has_product_name(self):
        self.assertIsNotNone(self.ac.product_name)
        self.assertIsInstance(self.ac.product_name, str)

    def test_that_Ac_can_Display_Error_When_Temperature_is_Below_Minimum(self):
        self.assertEqual(16, self.ac.temperature)




if __name__ == '__main__':
    unittest.main()
