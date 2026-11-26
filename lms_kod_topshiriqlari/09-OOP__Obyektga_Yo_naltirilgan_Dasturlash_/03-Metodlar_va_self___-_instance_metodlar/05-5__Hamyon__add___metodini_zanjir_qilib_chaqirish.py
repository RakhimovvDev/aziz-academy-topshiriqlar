class Wallet:
    def __init__(self, balance):
        self.balance = balance
    def add(self, x):
        self.balance += x 
        return self 
try:
    balance = int(input())
    a = int(input())
    b = int(input())
    if balance < 0 or a < 0 or b < 0:
        print("BAD")
    else:
        w = Wallet(balance)
        w.add(a).add(b)
        print(w.balance)
except ValueError:
    print("BAD")