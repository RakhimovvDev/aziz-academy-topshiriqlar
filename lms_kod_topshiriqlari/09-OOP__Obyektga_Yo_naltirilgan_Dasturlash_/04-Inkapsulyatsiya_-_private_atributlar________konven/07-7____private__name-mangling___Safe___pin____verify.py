class Safe:
    def __init__(self, pin):
        self.__pin = pin

    def verify(self, try_pin):
        if self.__pin == try_pin:
            return "OK"
        return "NO"

try:
    s = input().split()
    pin = s[0]
    try_pin = s[1] if len(s) > 1 else input().strip()

    if len(pin) == 4 and pin.isdigit() and len(try_pin) == 4 and try_pin.isdigit():
        safe = Safe(pin)
        print(safe.verify(try_pin))
    else:
        print("BAD")
except:
    print("BAD")