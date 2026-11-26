class Text:
    def __init__(self, base):
        self.base = base

    def append(self, suffix):
        self.base = self.base + suffix


base = input().strip()
suffix = input().strip()

if not base or not suffix:
    print("BAD")
else:
    t = Text(base)
    t.append(suffix)
    print(t.base)