class Account:
    def __init__(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance

try:
    balance = int(input().strip())
    if balance < 0:
        print("BAD")
    else:
        acc = Account(balance)
        print(acc.get_balance())
except:
    print("BAD")