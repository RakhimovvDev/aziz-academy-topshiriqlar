class Bank:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return True
        return False


try:
    balance = int(input())
    amount = int(input())
    if balance < 0:
        print("BAD")
    else:
        acc = Bank(balance)
        if acc.withdraw(amount):
            print(f"BAL={acc.balance}")
        else:
            print("BAD")
except ValueError:
    print("BAD")