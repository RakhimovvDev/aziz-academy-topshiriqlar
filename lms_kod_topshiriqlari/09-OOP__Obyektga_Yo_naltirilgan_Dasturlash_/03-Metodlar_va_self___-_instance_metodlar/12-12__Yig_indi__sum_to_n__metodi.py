class RangeSum:
    def __init__(self, base):
        self.base = base

    def sum_to(self, n):
        return self.base + sum(range(1, n + 1))


try:
    base = int(input())
    n = int(input())
    if n < 0:
        print("BAD")
    else:
        rs = RangeSum(base)
        print(rs.sum_to(n))
except ValueError:
    print("BAD")