class Todo:
    def __init__(self, items):
        self.items = items

    def add(self, item):
        self.items.append(item)


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

        new_item = input().strip()
        if not valid or not new_item:
            print("BAD")
        else:
            todo = Todo(items)
            todo.add(new_item)
            print(todo.items[-1])
except ValueError:
    print("BAD")