class Account:
    def __init__(self, balance):
        self._balance = balance

    def set_balance(self, new_balance):
        if new_balance >= 0:
            self._balance = new_balance
            return True
        return False

try:
    s = input().split()
    balance = int(s[0])
    new_balance = int(s[1] if len(s) > 1 else input().strip())

    if balance < 0 or new_balance < 0:
        print("BAD")
    else:
        acc = Account(balance)
        if acc.set_balance(new_balance):
            print(f"BAL={acc._balance}")
        else:
            print("BAD")
except:
    print("BAD")