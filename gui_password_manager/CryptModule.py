import json

def decrypt(encrypted_data, key):
    decrypted_data = []
    key_length = len(key)
    for row in encrypted_data:
        decrypted_row = []
        for item in row:
            decrypted_item = ''
            for char in item:
                key_char = key[len(decrypted_item) % key_length]
                decrypted_char = chr(((ord(char) - ord(key_char)) % 256))
                decrypted_item += decrypted_char
            decrypted_row.append(decrypted_item)
        decrypted_data.append(decrypted_row)
    return decrypted_data

def encrypt(data, key):
    encrypted_data = []
    key_length = len(key)
    for row in data:
        encrypted_row = []
        for item in row:
            encrypted_item = ''
            for char in item:
                key_char = key[len(encrypted_item) % key_length]
                encrypted_char = chr(((ord(char) + ord(key_char)) % 256))
                encrypted_item += encrypted_char
            encrypted_row.append(encrypted_item)
        encrypted_data.append(encrypted_row)
    return encrypted_data

def load_and_decrypt_from_json(filename, key):
    with open(filename, 'r') as file:
        encrypted_data = json.load(file)
        decrypted_data = decrypt(encrypted_data, key)
    return decrypted_data

def encrypt_and_save_to_json(filename, key, data_to_encrypt):
    encrypted_data = encrypt(data_to_encrypt, key)
    with open(filename, 'w') as file:
        json.dump(encrypted_data, file)

def initialize_json_file(filename):
    with open(filename, 'w') as file:
        json.dump([], file)
