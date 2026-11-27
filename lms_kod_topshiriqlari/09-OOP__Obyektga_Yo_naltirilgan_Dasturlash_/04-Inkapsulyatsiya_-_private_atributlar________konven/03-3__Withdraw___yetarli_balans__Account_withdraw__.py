class Account:
    def __init__(self, balance):
        self._balance = balance

    def withdraw(self, amount):
        if amount > 0 and self._balance >= amount:
            self._balance -= amount
            return True
        return False

try:
    s = input().split()
    balance = int(s[0])
    amount = int(s[1] if len(s) > 1 else input().strip())

    if balance < 0 or amount <= 0:
        print("BAD")
    else:
        acc = Account(balance)
        if acc.withdraw(amount):
            print(f"BAL={acc._balance}")
        else:
            print("BAD")
except:
    print("BAD")