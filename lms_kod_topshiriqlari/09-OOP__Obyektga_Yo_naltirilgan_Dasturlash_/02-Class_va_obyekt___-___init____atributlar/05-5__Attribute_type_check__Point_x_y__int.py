class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
        
        
try:
    x_input = int(input())
    y_input = int(input())
    
    p = Point(x_input, y_input)
    
    if isinstance(p.x, int) and isinstance(p.y, int) and not isinstance(p.x, bool) and not isinstance(p.y, bool):
        print(f"X={p.x} Y={p.y}")
    else:
        print("BAD")
        
except ValueError:
    print("BAD")