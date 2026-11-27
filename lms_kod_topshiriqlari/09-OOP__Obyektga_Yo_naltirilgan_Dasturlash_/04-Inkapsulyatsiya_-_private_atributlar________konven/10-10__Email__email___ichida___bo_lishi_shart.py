class Email:
    def __init__(self, email):
        self._email = email

    def set_email(self, x):
        self._email = x

    def get_email(self):
        return self._email

try:
    e1 = input().strip()
    e2 = input().strip()

    if not e1 or "@" not in e1 or not e2 or "@" not in e2:
        print("BAD")
    else:
        em = Email(e1)
        em.set_email(e2)
        print(em.get_email())
except:
    print("BAD")