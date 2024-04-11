import csv
import base64
from cryptography.fernet import Fernet
import os
import key_manager as km
class Database:
    def __init__(self,password):
        self.master_password=password
        if not check_file_existence('db_key.key'):
            km.generate_and_save_key(self.master_password)
        self.key = km.get_key(self.master_password)
        self.cipher_suite = Fernet(self.key)
        self.filename = "database.csv"
    def _encrypt_data(self, data):
        encrypted_data = self.cipher_suite.encrypt(data.encode())
        return base64.b64encode(encrypted_data).decode()

    def _decrypt_data(self, encrypted_data):
        decrypted_data = self.cipher_suite.decrypt(base64.b64decode(encrypted_data)).decode()
        return decrypted_data

    def initialize_database(self):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Wpisanie głównego hasła jako pierwszego rekordu
            encrypted_master_password = self._encrypt_data(self.master_password)
            writer.writerow([encrypted_master_password])

    def add_entry(self, website, username, password):
        encrypted_website = self._encrypt_data(website)
        encrypted_username = self._encrypt_data(username)
        encrypted_password = self._encrypt_data(password)

        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([encrypted_website, encrypted_username, encrypted_password])

    def delete_entry(self, index):
        rows = []
        with open(self.filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                rows.append(row)
        index=index+1
        if 0 <= index < len(rows):
            del rows[index]
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                for row in rows:
                    writer.writerow(row)
        else:
            print("Index out of range")

    def get_password(self):
        with open(self.filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            encrypted_password = next(reader)[0]  # Odczytanie zaszyfrowanego hasła z pierwszego wiersza
            return self._decrypt_data(encrypted_password)
        
    def get_data(self):
        decrypted_entries = []
        with open(self.filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for idx, row in enumerate(reader):
                decrypted_website = self._decrypt_data(row[0])
                decrypted_username = self._decrypt_data(row[1])
                decrypted_password = self._decrypt_data(row[2])
                decrypted_entries.append([idx, decrypted_website, decrypted_username, decrypted_password])
        return decrypted_entries

    def modify_entry(self, index, website, username, password):
        rows = []
        with open(self.filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                rows.append(row)

        if 0 <= index < len(rows):
            encrypted_website = self._encrypt_data(website)
            encrypted_username = self._encrypt_data(username)
            encrypted_password = self._encrypt_data(password)

            rows[index] = [encrypted_website, encrypted_username, encrypted_password]

            with open(self.filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                for row in rows:
                    writer.writerow(row)
        else:
            print("Index out of range")

def check_file_existence(filename):
    return os.path.isfile(filename)

# Przykład użycia
'''
key = b'j4jyQPzZ-APGxK1j3_mmQjgbqQtWefR598wr4zwHvJM='  # Możesz wygenerować własny klucz
db = Database(key)
db.initialize_database("haslo123")
# Dodawanie wpisów do bazy danych
db.add_entry("www.example.com", "user123", "password123")
#db.write_to_database("www.anotherexample.com", "admin", "securepassword")
# Wyświetlenie zdeszyfrowanych danych
decrypted_data = db.get_data()
for entry in decrypted_data:
    print(entry)

print(db.get_password())
'''