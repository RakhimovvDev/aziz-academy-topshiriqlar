class Rectangle:
    def __init__(self, w, h):
        self.w = w 
        self.h = h 
    def area(self):
        return self.w * self.h 
    def perimeter(self):
        return 2 * (self.w + self.h)
try:
    w = int(input())
    h = int(input())
    if w <= 0 or h <= 0:
        print("BAD")
    else:
        r = Rectangle(w, h)
        print(f"A={r.area()}")
        print(f"P={r.perimeter()}")
except ValueError:
    print("BAD")