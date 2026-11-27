class Password:
    def __init__(self, pwd):
        self.__pwd = pwd

    def check(self, x):
        return self.__pwd == x

try:
    p1 = input().strip()
    p2 = input().strip()

    if len(p1) < 6 or len(p2) < 6:
        print("BAD")
    else:
        p = Password(p1)
        if p.check(p2):
            print("OK")
        else:
            print("NO")
except:
    print("BAD")