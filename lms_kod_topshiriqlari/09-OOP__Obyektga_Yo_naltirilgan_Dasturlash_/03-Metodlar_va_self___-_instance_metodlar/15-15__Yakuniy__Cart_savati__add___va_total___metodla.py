class Cart:
    def __init__(self):
        self.items = {}

    def add(self, name, price, qty):
        if name in self.items:
            if self.items[name][0] != price:
                return False
            self.items[name][1] += qty
        else:
            self.items[name] = [price, qty]
        return True

    def total(self):
        return sum(price * qty for price, qty in self.items.values())


try:
    q = int(input())
    if q < 0:
        print("BAD")
    else:
        cart = Cart()
        outputs = []
        ok = True

        for _ in range(q):
            parts = input().split()
            if not parts:
                ok = False
                break

            cmd = parts[0]
            if cmd == "ADD":
                if len(parts) != 4:
                    ok = False
                    break
                name = parts[1].strip()
                price = int(parts[2])
                qty = int(parts[3])
                if not name or price < 0 or qty <= 0:
                    ok = False
                    break
                if not cart.add(name, price, qty):
                    ok = False
                    break
            elif cmd == "TOTAL":
                if len(parts) != 1:
                    ok = False
                    break
                outputs.append(str(cart.total()))
            else:
                ok = False
                break

        if not ok:
            print("BAD")
        else:
            for line in outputs:
                print(line)
except ValueError:
    print("BAD")