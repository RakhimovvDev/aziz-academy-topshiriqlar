class Config:
    theme = "light"
try:
    mode = input().strip()
    obj = Config()
    
    if mode == "CLASS":
        Config.theme = "dark"
    elif mode == "INSTANCE":
        obj.theme = "dark"
    else:
        raise ValueError("Noto'g'ri mode")
    print(f"CLASS={Config.theme} OBJ={obj.theme}")
except (ValueError, EOFError):
    print("BAD")