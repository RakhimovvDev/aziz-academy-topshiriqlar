class Counter:
    def __init__(self, value):
        self.value = value 
    def inc(self):
        self.value += 1
        
try:
    start = int(input())
    n = int(input())
    if n < 0:
        print("BAD")
    else:
        c = Counter(start)
        for _ in range(n):
            c.inc()
        print(c.value)
except ValueError:
    print("BAD")