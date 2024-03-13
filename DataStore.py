import json
import CryptModule as cm
import os

class Database:
    def __init__(self, db_name, pwd):
        self.name=db_name
        self.pwd=pwd

    def create_database(self):
        file=self.name+".json"
        cm.initialize_json_file(file)
        credentials= [self.name, self.pwd]
        cm.encrypt_and_save_to_json(file, self.pwd, credentials)
        
    def write_to_database(self, datalist):
        file=self.name+".json"
        # Wczytanie i deszyfrowanie danych z pliku JSON
        decrypted_data = cm.load_and_decrypt_from_json(file, self.pwd)
        # Dodanie nowego wiersza do danych
        new_row = datalist
        decrypted_data.append(new_row)
        #print(decrypted_data[6])
        # Szyfrowanie i zapisywanie danych do pliku JSON
        cm.encrypt_and_save_to_json(file, self.pwd, decrypted_data)

    def read_from_database(self):
        file=self.name+".json"
        data=cm.load_and_decrypt_from_json(file, self.pwd)
        data=data[2:]
        return data


test=Database("pls", "PAsswords_23^")  
#test.create_database()
test.write_to_database(["haselko", "tftft","git.pl"])
print(test.read_from_database())