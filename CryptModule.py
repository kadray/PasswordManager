from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad
import csv
import io

# Function to encrypt CSV data and write it to a file
def encrypt_data(data, output_file, password):
    # Convert data to CSV format
    csv_data = io.StringIO()
    writer = csv.writer(csv_data)
    writer.writerows(data) #tu zmieniłem
    csv_data.seek(0)
    csv_bytes = csv_data.read().encode()

    # Generate a key from the password using PBKDF2
    salt = get_random_bytes(16)
    key = PBKDF2(password, salt, dkLen=32, count=1000000)

    # Initialize AES cipher in CBC mode
    cipher = AES.new(key, AES.MODE_CBC)

    # Write the salt and IV to the beginning of the output file
    with open(output_file, 'wb') as f:
        f.write(salt)
        f.write(cipher.iv)

        # Pad the data to fit the block size of AES
        padded_data = pad(csv_bytes, AES.block_size)

        # Encrypt the data
        encrypted_data = cipher.encrypt(padded_data)
        f.write(encrypted_data)

# Function to decrypt a CSV file and return the data as a list
def decrypt_csv(input_file, password):
    # Open the input file and read the salt and IV
    with open(input_file, 'rb') as f:
        salt = f.read(16)
        iv = f.read(16)

        # Generate key from the password and salt using PBKDF2
        key = PBKDF2(password, salt, dkLen=32, count=1000000)

        # Initialize AES cipher in CBC mode
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)

        # Read the encrypted data from the file
        encrypted_data = f.read()

        # Decrypt the data
        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

        # Convert decrypted bytes to CSV format
        decrypted_str = decrypted_data.decode()
        csv_data = io.StringIO(decrypted_str)
        reader = csv.reader(csv_data)
        decrypted_list = list(reader)

        return decrypted_list


# Example usage:
'''
data_to_encrypt = [
    ['Name', 'Age', 'Country'],
    ['John', '25', 'USA'],
    ['Alice', '30', 'Canada']
]

encrypt_data(data_to_encrypt, 'encrypted.csv', 'mypassword')
decrypted_data = decrypt_csv('encrypted.csv', 'mypassword')
encrypt_data(decrypt_csv('encrypted.csv', "mypassword"),"test.csv", "mypassword")
print(decrypted_data)
'''
