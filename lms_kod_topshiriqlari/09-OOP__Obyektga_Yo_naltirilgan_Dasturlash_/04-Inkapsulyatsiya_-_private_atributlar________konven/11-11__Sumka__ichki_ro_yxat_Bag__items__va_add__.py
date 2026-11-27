class Bag:
    def __init__(self, items=None):
        self._items = items if items else []

    def add(self, item):
        self._items.append(item)

    def count(self):
        return len(self._items)

try:
    n = int(input().strip())
    if n < 0:
        print("BAD")
    else:
        items = []
        for _ in range(n):
            item = input().strip()
            if not item:
                raise ValueError
            items.append(item)

        new_item = input().strip()
        if not new_item:
            raise ValueError

        bag = Bag(items)
        bag.add(new_item)
        print(bag.count())
except:
    print("BAD")