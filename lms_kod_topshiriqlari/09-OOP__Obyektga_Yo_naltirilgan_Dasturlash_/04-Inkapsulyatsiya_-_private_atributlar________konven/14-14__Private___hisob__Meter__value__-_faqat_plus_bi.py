class Meter:
    def __init__(self, value):
        self._value = value

    def plus(self, x):
        if x > 0:
            self._value += x
            return True
        return False

    def value(self):
        return self._value

try:
    s = input().split()
    start = int(s[0])
    add_val = int(s[1] if len(s) > 1 else input().strip())

    if start < 0 or add_val <= 0:
        print("BAD")
    else:
        m = Meter(start)
        m.plus(add_val)
        print(m.value())
except:
    print("BAD")