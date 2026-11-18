class Person:
    def __init__(self, full_name):
        cleaned = full_name.strip()
        if not cleaned:
            raise ValueError("Bo'sh satr")
        self.name = cleaned.title()
        
try:
    full_name_input = input()
    p = Person(full_name_input)   
    print(p.name)
except (ValueError, EOFError):
    print("BAD")