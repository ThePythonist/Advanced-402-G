class BankAccount:
    def __init__(self, id, name, type, limit):
        self.id = id
        self.name = name
        self.type = type
        self.limit = limit
        self.balance = 0

    def show_balance(self):
        print(f"Current account balance : {self.balance}")

    def deposit(self):
        value = int(input("Deposit value : "))
        self.balance += value
        print(f"Deposit : {value}")
        print(f"Current account balance : {self.balance}")
        print('-' * 50)

    def withdraw(self):
        value = int(input("Withdraw value : "))
        if self.balance > value:
            self.balance -= value
            print(f"Withdraw : {value}")
            print(f"Current account balance : {self.balance}")
            print('-' * 50)
        else:
            print("Your account balance is not enough")
            print('-' * 50)


customer1 = BankAccount(1111, "Mamad", "Seporde Kotah Modat", 50000)
customer2 = BankAccount(1111, "Kiana", "Seporde Boland Modat", 50000)


def main():
    transaction = input("""
    1 : Deposit
    2 : Withdraw
    3 : Show Balance
    """)

    if transaction == "1":
        customer1.deposit()
        main()
    elif transaction == "2":
        customer1.withdraw()
        main()
    elif transaction == "3":
        customer1.show_balance()
        main()
    else:
        print("Invalid Transaction")
        main()


main()
