class Atm_Transaction:

    def __init__(self, withdrawal: int, balance: int, transfer: int, pay_bills: int, PIN: int, account_number: int):
        self.balance = balance
        self.withdrawal = withdrawal
        self.transfer = transfer
        self.pay_bills = pay_bills
        self.PIN = PIN
        self.account_number = account_number


union_bank = Atm_Transaction(3000, 5000, 1000, 200, 1234, 0000000)

while True:
    print("Welcome to Union bank")
    pin = int(input("Enter PIN :"))
    if pin == union_bank.PIN:

        print("choose 1 to withdrawal")
        print("choose 2 to check Balance")
        print("choose 3 to Transfer ")
        print("choose 5 to pay_bills")
        print("choose 6 to Cancel")
        kata = int(input())
        if kata == 6:
            break
        if kata == 1:
            print("welcome to withdraw section")
            amount = int(input("Enter amount: "))
            if amount < union_bank.balance:
                union_bank.balance -= amount
                print("withdraw successful")
                print("Your new balance is", union_bank.balance)
            else:
                print("Insufficient balance")

        if kata == 2:
            print("Check Balance")
            print("Balance is ", union_bank.balance)

        if kata == 3:
            print("Ready to Transfer ?")
            account_number = int(input("Enter Account_Number: "))
            print("Choose Bank to Transfer")
            print("Press 1 to Access Bank")
            print("press 2 to First Bank")
            print("Press 3 to Zenith Bank")
            transfer = int(input())
            if transfer == 0:
                break

            if transfer == 1:
                print(" Choose Access Bank")
                print("Transaction Successful")

            if transfer == 2:
                print(" Choose First Bank")
                print("Transaction Successful")

            if transfer == 3:
                print(" Choose Zenith Bank")
    else:
        print("Invalid Pin")
