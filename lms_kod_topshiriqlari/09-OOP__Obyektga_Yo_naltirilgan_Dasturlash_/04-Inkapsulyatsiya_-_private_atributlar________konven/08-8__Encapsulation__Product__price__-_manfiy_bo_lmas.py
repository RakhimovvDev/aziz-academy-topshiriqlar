class Product:
    def __init__(self, price):
        self._price = price

    def set_price(self, x):
        if x >= 0:
            self._price = x
            return True
        return False

    def get_price(self):
        return self._price

try:
    s = input().split()
    p1 = int(s[0])
    p2 = int(s[1] if len(s) > 1 else input().strip())

    if p1 < 0 or p2 < 0:
        print("BAD")
    else:
        p = Product(p1)
        if p.set_price(p2):
            print(f"PRICE={p.get_price()}")
        else:
            print("BAD")
except:
    print("BAD")