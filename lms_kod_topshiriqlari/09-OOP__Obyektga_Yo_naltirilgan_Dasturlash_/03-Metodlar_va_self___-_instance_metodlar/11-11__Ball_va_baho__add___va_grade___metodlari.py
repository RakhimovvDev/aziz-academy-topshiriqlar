class Score:
    def __init__(self, value):
        self.value = value

    def add(self, points):
        self.value += points

    def grade(self):
        if self.value >= 90:
            return "A"
        elif self.value >= 70:
            return "B"
        elif self.value >= 50:
            return "C"
        return "D"


try:
    start = int(input())
    points = int(input())
    if start < 0 or start > 100:
        print("BAD")
    else:
        s = Score(start)
        s.add(points)
        if s.value < 0 or s.value > 100:
            print("BAD")
        else:
            print(s.grade())
except ValueError:
    print("BAD")