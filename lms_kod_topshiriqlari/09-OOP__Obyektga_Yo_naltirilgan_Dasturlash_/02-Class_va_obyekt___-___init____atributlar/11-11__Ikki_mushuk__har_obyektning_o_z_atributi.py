class Mushuk:
    def __init__(self, ism, yosh):
        self.ism = ism 
        self .yosh = yosh 
        
        
ism1 = input().strip()
yosh1 = int(input().strip())
ism2 = input().strip()
yosh2 = int(input().strip())

m1 = Mushuk(ism1, yosh1)
m2 = Mushuk(ism2, yosh2)


m1.yosh += 1

print(f"{m1.ism} {m1.yosh}")
print(f"{m2.ism} {m2.yosh}")