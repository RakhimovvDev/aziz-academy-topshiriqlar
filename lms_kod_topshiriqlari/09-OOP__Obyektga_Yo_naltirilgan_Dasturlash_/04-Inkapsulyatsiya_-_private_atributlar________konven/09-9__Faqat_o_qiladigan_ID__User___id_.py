class User:
    def __init__(self, user_id):
        self.__id = user_id

    @property
    def id(self):
        return self.__id

try:
    uid = int(input().strip())
    if uid <= 0:
        print("BAD")
    else:
        user = User(uid)
        print(f"ID={user.id}")
except:
    print("BAD")