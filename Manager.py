#User
import os
import csv
import re 
import CryptModule as cm
import DataStore as ds

def initialize_database():
    db_name=input("Nazwa Bazy Danych: ")
    pwd=input("Hasło: ")
    while not validate_password(pwd):
        pwd=input("Hasło: ")
    test =ds.Database(db_name, pwd)
    test.create_database()

def validate_password(pwd):
    # Check if password has at least 8 characters
    if len(pwd) < 8:
        return False
    
    # Check if password has at least one special character
    if not any(char in '.,!@#$%^&*/()[]{}-_=+' for char in pwd):
        return False
    
    # Check if password has at least one digit
    if not re.search(r'\d', pwd):
        return False
    
    # Check if password has at least one capital letter
    if not re.search(r'[A-Z]', pwd):
        return False
    
    return True

initialize_database()