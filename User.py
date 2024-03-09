#User
import CryptModule as em
class User:
    def __init__(self, username, password):
        self.username=em.encrypt(username, 5)
        self.password=em.encrypt(password, 10)
