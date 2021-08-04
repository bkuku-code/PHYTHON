import unittest

import self as self

from account import Account

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.account1 = Account("name" , "081123" , 100.00, "0786" , "savings")

    def test_something(self):
        self.assertEqual(True, True)

    def test_account_has_number(self):
        self.assertIsNotNone(self.account1.number)
        self.assertIsNotNone(self.account1.number,str)

    def test_account_has_name(self):
        self.assertIsNotNone(self.account1.name)
        self.assertIsNotNone(self.account1.name,str)

    def test_account_has_balance(self):
        self.assertIsNotNone(self.account1.balance)
        self.assertIsNotNone(self.account1.balance,str)

    def test_account_has_acct_type(self):
        self.assertIsNotNone(self.account1.acct_type)
        self.assertIsNotNone(self.account1.acct_type,str)

    def test_account_has_pin(self):
        self.assertIsNotNone(self.account1.pin)
        self.assertIsNotNone(self.account1.pin,str)

    def test_account_has_withdrwal(self):
        self.account1.withdrwal, (0.0 ,"2311")

    def test_account1_can_withdrawl_above_balance(self):
        self.assertRaises(Exception,self.account1.withdrwal, (100.0, "2311"))


    def test_account1_can_withdrawl_less_than_balance(self):
        self.assertRaises(Exception, self.account1.withdrwal, (-100.0, "2311"))









if __name__ == '__main__':
    unittest.main()
