def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        encrypted_text += chr(ord(char) + key)
    return encrypted_text

def decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        decrypted_text += chr(ord(char) - key)
    return decrypted_text
