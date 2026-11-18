class Student:
    school = "PDP"
    
    def __init__(self, name):
        cleaned_name = name.strip()
        if not cleaned_name:
            raise ValueError("")
        self.name = cleaned_name
        
try:
    name_input = input()
    s = Student(name_input)
    print(f"{s.name} @ {s.school}")
except (ValueError, EOFError):
    print("BAD")