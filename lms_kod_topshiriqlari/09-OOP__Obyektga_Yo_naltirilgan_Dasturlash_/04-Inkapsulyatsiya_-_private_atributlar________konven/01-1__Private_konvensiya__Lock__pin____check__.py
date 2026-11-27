class Lock:
    def __init__(self, pin):
        self._pin = pin

    def check(self, try_pin):
        if self._pin == try_pin:
            return "OK"
        return "NO"

try:
    s = input().split()
    pin = s[0]
    try_pin = s[1] if len(s) > 1 else input().strip()

    if len(pin) == 4 and pin.isdigit() and len(try_pin) == 4 and try_pin.isdigit():
        lock = Lock(pin)
        print(lock.check(try_pin))
    else:
        print("BAD")
except:
    print("BAD")