from cryptography.fernet import Fernet
import hashlib
import base64
def generate_key():
    key = Fernet.generate_key()
    return key

def generate_key_from_seed(seed):
    # Convert the seed string to bytes
    seed_bytes = bytes(seed, 'utf-8')
    # Use a hash function to create a 32-byte key from the seed
    key = hashlib.sha256(seed_bytes).digest()
    # Encode the key using URL-safe base64 encoding
    encoded_key = base64.urlsafe_b64encode(key)
    return encoded_key


def _encrypt(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message)
    with open("db_key.key", "wb") as file:
        file.write(encrypted_message)

def _decrypt(key):
    f = Fernet(key)
    with open("db_key.key", "rb") as file:
        encrypted_message = file.read()
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message

def string_to_bytes(string):
    return bytes(string, 'utf-8')

def generate_and_save_key(password):
    db_key=generate_key()
    user_password=generate_key_from_seed(password)
    _encrypt(db_key, user_password)

def get_key(password):
    key=generate_key_from_seed(password)
    return _decrypt(key)


