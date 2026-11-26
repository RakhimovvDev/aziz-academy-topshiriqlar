class User:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
    def is_adult(self):
        return self.age >= 18 
name = input().strip()
try:
    age = int(input())
    if not name or age < 0 or age > 120:
        print("BAD")
    else:
        u = User(name, age)
        print("ADULT" if u.is_adult() else "MINOR")
except  ValueError:
    print("BAD")