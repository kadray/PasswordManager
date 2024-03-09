def encrypt(text, ):
    shift=10
    """Encrypts ASCII characters using a Caesar cipher with a given shift."""
    encrypted_text = ""
    for char in text:
        # Check if the character is an ASCII character
        if ord(char) >= 32 and ord(char) <= 126:
            # Calculate the new ASCII value after shifting
            encrypted_ascii = ord(char) + shift
            # Wrap around if the new ASCII value goes beyond printable ASCII range
            if encrypted_ascii > 126:
                encrypted_ascii -= 95
            encrypted_text += chr(encrypted_ascii)
        else:
            # Preserve non-printable ASCII characters as they are
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text):
    shift=10
    """Decrypts ASCII characters encrypted using a Caesar cipher with a given shift."""
    decrypted_text = ""
    for char in encrypted_text:
        # Check if the character is an ASCII character
        if ord(char) >= 32 and ord(char) <= 126:
            # Calculate the original ASCII value before shifting
            decrypted_ascii = ord(char) - shift
            # Wrap around if the original ASCII value goes beyond printable ASCII range
            if decrypted_ascii < 32:
                decrypted_ascii += 95
            decrypted_text += chr(decrypted_ascii)
        else:
            # Preserve non-printable ASCII characters as they are
            decrypted_text += char
    return decrypted_text