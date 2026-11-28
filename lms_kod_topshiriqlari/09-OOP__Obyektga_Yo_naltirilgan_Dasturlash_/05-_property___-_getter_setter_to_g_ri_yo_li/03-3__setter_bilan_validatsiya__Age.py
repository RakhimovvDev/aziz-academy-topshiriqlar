class Person:
    def __init__(self, age=0):
        self.age = age 
        
    @property 
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            self._age = 0 
        else:
            self._age = value 
            
            
n = int(input().strip())
p = Person()
p.age = n 
print(p.age)