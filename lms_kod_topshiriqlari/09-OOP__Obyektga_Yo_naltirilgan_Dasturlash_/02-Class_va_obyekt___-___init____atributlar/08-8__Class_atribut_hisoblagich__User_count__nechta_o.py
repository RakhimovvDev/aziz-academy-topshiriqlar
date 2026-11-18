class User:
    count = 0 
    
    def __init__(self, username):
        cleaned = username.strip()
        if not cleaned:
            raise ValueError("")
        self.username = cleaned
        User.count += 1
        
try:
    n = int(input())
    if n < 0:
        raise ValueError("")
    for _ in range(n):
        uname = input()
        User(uname)
        
    print(f"COUNT={User.count}")
except (ValueError, EOFError):
    print("BAD")