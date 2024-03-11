import csv
import os
import CryptModule as cm

# input -> nazwa bazy danych, LISTA danych do wpisania | output-> wpisanie danych do kolejnego wiersza
def write_to_database(db_name, datalist):
    file="databases/"+db_name+".csv"
    with open(file, mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(datalist)
        csv_file.close()


# input -> nazwa bazy danych, index wiersza do usunięcia | output -> usunięcie wpisu i przesunięcie wszystkiego aby zapełnić dziure
def remove_from_database(db_name, index):
    # Wczytaj dane z pliku CSV
    file="databases/"+db_name+".csv"
    with open(file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        data = list(reader)
    # Usuń wiersz o określonym indeksie
    del data[index]
    # Zapisz zaktualizowane dane z powrotem do pliku CSV
    with open(file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)
        csv_file.close()


# input -> nazwa bazy danych do utworzenia | output -> utworzenie pliku csv
def create_database(db_name, pwd):
        file="databases/"+db_name+".csv"
        if not os.path.exists(file):
            # Plik nie istnieje, więc zostanie utworzony
            with open(file, 'w', newline='') as csv_file:
                csv_file.close()
            cm.encrypt_data([db_name, pwd], file, pwd)

def add_record_to_encrypted_csv(input_file, output_file, password, new_record):
    # Decrypt the encrypted CSV file to get the existing data
    existing_data = cm.decrypt_csv(input_file, password)
    
    # Add the new record to the existing data
    existing_data.append(new_record)
    
    # Encrypt the updated data and write it to the output file
    cm.encrypt_data(existing_data, output_file, password)

def get_data(input_file, password):
    decrypted_list= cm.decrypt_csv(input_file, password)
    strings = [''.join(inner_list) for inner_list in decrypted_list]
    result = ' '.join(strings)
    return result
create_database("baza", "haselko")


add_record_to_encrypted_csv("databases/baza.csv", "databases/baza.csv", "haselko", ["login2", "haslo2"])
print(cm.decrypt_csv("databases/baza.csv", "haselko"))
print(get_data("databases/baza.csv", "haselko"))