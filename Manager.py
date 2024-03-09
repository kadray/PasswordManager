#User
import os
import csv
import re # to jest regex chyba
import CryptModule as cm



'''
#to do zmiany
def change_password(old_pwd, new_pwd):
    if old_pwd!=cm.decrypt(password):
        return False
    self.password=cm.encrypt(new_pwd)
    return True
'''

def validate_password(password):
    # Check if password has at least 8 characters
    if len(password) < 8:
        return False
    
    # Check if password has at least one special character
    if not any(char in '.,!@#$%^&*/()[]{}-_=+' for char in password):
        return False
    
    # Check if password has at least one digit
    if not re.search(r'\d', password):
        return False
    
    # Check if password has at least one capital letter
    if not re.search(r'[A-Z]', password):
        return False
    
    return True
