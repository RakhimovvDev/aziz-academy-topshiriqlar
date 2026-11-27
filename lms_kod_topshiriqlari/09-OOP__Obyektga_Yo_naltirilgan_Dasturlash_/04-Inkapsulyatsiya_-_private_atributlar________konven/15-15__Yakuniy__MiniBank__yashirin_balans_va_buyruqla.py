class MiniBank:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, x):
        if x > 0:
            self.__balance += x
            return True
        return False

    def withdraw(self, x):
        if 0 < x <= self.__balance:
            self.__balance -= x
            return True
        return False

    @property
    def balance(self):
        return self.__balance

try:
    initial_bal = int(input().strip())
    q = int(input().strip())

    if initial_bal < 0 or q < 0:
        print("BAD")
    else:
        bank = MiniBank(initial_bal)
        ok = True

        for _ in range(q):
            parts = input().split()
            if len(parts) != 2:
                ok = False
                break
            cmd, val = parts[0], int(parts[1])
            if val <= 0:
                ok = False
                break

            if cmd == "DEP":
                if not bank.deposit(val):
                    ok = False
                    break
            elif cmd == "WDR":
                if not bank.withdraw(val):
                    ok = False
                    break
            else:
                ok = False
                break

        if ok:
            print(f"BAL={bank.balance}")
        else:
            print("BAD")
except:
    print("BAD")