from Exception import NegativeAmountException, insufficientBalanceException


class Account:
    def __init__(self, name: str, number: str, balance: float, pin: str, acct_type: str):
        self.name = name
        self.number = number
        self.balance = balance
        self.pin = pin
        self.acct_type = acct_type

    def withdrwal(self, amount: float, pin: str) -> None:
        if amount < 0:
            raise NegativeAmountException()
        if self.balance < amount:
            raise insufficientBalanceException()
        if self.balance >= amount:
            self.balance -= amount

    def deposit(self, amount: float) -> None:
        pass

    def transfer(self, account_number: str, amount: float, pin: str) -> None:
        pass

    def change_pin(self, old_pin: str, new_pin: str) -> None:
        pass
