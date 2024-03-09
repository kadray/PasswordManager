import csv
import os
import CryptModule as cm

def write_to_database(username, datalist):
    file="databases/"+username+".csv"
    for i in range(len(datalist)):
        datalist[i]=cm.encrypt(datalist[i])
    with open(file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(datalist)
            file.close()

def create_database(username):
    db_name="databases/"+username+".csv"
    if not os.path.exists(db_name):
        # Plik nie istnieje, więc zostanie utworzony
        with open(db_name, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            # Możesz tutaj opcjonalnie dodać nagłówki lub początkowe dane
            return True
    else:
        return False