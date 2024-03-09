import Manager as mg
import CryptModule as cm
import DataStore as ds

def register_user():
    usr=input("Login: ")
    pwd=input("Hasło: ")
    while not mg.validate_password(pwd):
            pwd=input("Hasło: ")
    ds.create_database(usr)
    ds.write_to_database(usr, [usr, pwd])

register_user()
