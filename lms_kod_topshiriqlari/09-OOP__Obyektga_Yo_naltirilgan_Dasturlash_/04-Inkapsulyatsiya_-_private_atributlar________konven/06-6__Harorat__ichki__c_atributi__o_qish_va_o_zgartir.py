class Temperature:
    def __init__(self, c):
        self._c = c

    @property
    def celsius(self):
        return self._c

    @celsius.setter
    def celsius(self, value):
        self._c = value

try:
    c1 = int(input().strip())
    c2 = int(input().strip())

    t = Temperature(c1)
    t.celsius = c2
    print(f"C={t.celsius}")
except:
    print("BAD")