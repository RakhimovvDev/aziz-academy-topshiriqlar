class Timer:
    def __init__(self, seconds):
        self.seconds = seconds

    def tick(self):
        if self.seconds > 0:
            self.seconds -= 1
        return self.seconds


try:
    seconds = int(input())
    k = int(input())
    if seconds < 0 or k < 0:
        print("BAD")
    else:
        t = Timer(seconds)
        for _ in range(k):
            t.tick()
        print(t.seconds)
except ValueError:
    print("BAD")