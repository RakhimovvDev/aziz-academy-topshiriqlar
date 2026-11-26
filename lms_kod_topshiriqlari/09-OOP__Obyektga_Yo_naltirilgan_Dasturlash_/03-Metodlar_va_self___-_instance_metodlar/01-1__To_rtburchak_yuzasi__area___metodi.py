class Rectangle:
    def __init__(self, w, h):
        self.w = w 
        self.h = h 
    def area(self):
        return self.w * self.h 
try:
    w = int(input())
    h = int(input())
    if w <= 0 or h <= 0:
        print("BAD")
    else:
        r = Rectangle(w, h)
        print(r.area())
except  ValueError:
    print("BAD")