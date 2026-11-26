class Circle:
    def __init__(self, r):
        self.r = r
    def circumference(self):
        return int(2 * 3.14 * self.r)
    
try:
    r = int(input())
    if r <= 0:
        print("BAD")
    else:
        c = Circle(r)
        print(c.circumference())
except ValueError:
    print("BAD")