class Inventory:
    def __init__(self, items):
        self.items = items

    def remove(self, target):
        if target in self.items:
            self.items.remove(target)
            return True
        return False


try:
    n = int(input())
    if n < 0:
        print("BAD")
    else:
        items = []
        valid = True
        for _ in range(n):
            item = input().strip()
            if not item:
                valid = False
            items.append(item)

        target = input().strip()
        if not valid or not target:
            print("BAD")
        else:
            inv = Inventory(items)
            if inv.remove(target):
                print("REMOVED")
            else:
                print("NOTFOUND")
except ValueError:
    print("BAD")