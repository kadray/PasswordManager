import json
import CryptModule as cm
import os
import re

class Database:
    def __init__(self, db_name, pwd):
        self.name=db_name
        self.pwd=pwd


    def create_database(self):
        file = self.name + ".json"
        # Sprawdzenie istnienia pliku
        if not os.path.exists(file):
            cm.initialize_json_file(file)
            credentials = [self.name, self.pwd]
            cm.encrypt_and_save_to_json(file, self.pwd, [credentials])
        

    def write_to_database(self, datalist):
        file=self.name+".json"
        # Wczytanie i deszyfrowanie danych z pliku JSON
        decrypted_data = cm.load_and_decrypt_from_json(file, self.pwd)
        # Dodanie nowego wiersza do danych
        new_row = datalist
        decrypted_data.append(new_row)
        # Szyfrowanie i zapisywanie danych do pliku JSON
        cm.encrypt_and_save_to_json(file, self.pwd, decrypted_data)


    def read_from_database(self):
        file=self.name+".json"
        data=cm.load_and_decrypt_from_json(file, self.pwd)
        data=data[1:]
        return data
    
    def delete_from_database(self, index):
        file = self.name + ".json"
        # Wczytanie i deszyfrowanie danych z pliku JSON
        decrypted_data = cm.load_and_decrypt_from_json(file, self.pwd)
        
        # Sprawdzenie, czy indeks jest prawidłowy
        if index < 0 or index >= len(decrypted_data):
            print("Nieprawidłowy indeks.")
            return
        
        # Usunięcie wpisu o podanym indeksie
        del decrypted_data[index]
        
        # Szyfrowanie i zapisywanie zaktualizowanych danych do pliku JSON
        cm.encrypt_and_save_to_json(file, self.pwd, decrypted_data)


    def get_data_with_indices(self):
        file = self.name + ".json"
        # Wczytanie i deszyfrowanie danych z pliku JSON
        decrypted_data = cm.load_and_decrypt_from_json(file, self.pwd)
        decrypted_data=decrypted_data[1:]
        # Tworzenie listy zawierającej krotki (indeks wiersza, dane)
        data_with_indices = []
        for index, row in enumerate(decrypted_data):
            data_with_indices.append((index+1, *row))
        
        return data_with_indices
    

    def modify_entry(self, index, new_data):
        file = self.name + ".json"
        # Wczytanie i deszyfrowanie danych z pliku JSON
        decrypted_data = cm.load_and_decrypt_from_json(file, self.pwd)
        
        # Sprawdzenie, czy indeks jest prawidłowy
        if index < 0 or index >= len(decrypted_data):
            print("Nieprawidłowy indeks.")
            return
        
        # Modyfikacja wpisu o podanym indeksie
        decrypted_data[index] = new_data
        
        # Szyfrowanie i zapisywanie zaktualizowanych danych do pliku JSON
        cm.encrypt_and_save_to_json(file, self.pwd, decrypted_data)


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


def initialize_database():
    db_name=input("Nazwa Bazy Danych: ")
    pwd=input("Hasło: ")
    while not validate_password(pwd):
        pwd=input("Hasło: ")
    test =Database(db_name, pwd)
    test.create_database()
'''
test=Database("bazaaa", "haslo")
#test.create_database()
test.write_to_database(["strona2", "LOGIN", "haslo"])
print(test.get_data_with_indices())
'''