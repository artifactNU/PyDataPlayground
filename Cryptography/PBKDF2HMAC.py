# Password-based encryption is a technique that derives encryption keys from user passwords.
# It ensures that only users with the correct password can decrypt the data.
# PBKDF2HMAC (Password-Based Key Derivation Function 2 with HMAC) is used to derive the encryption key securely.
# Fernet is a symmetric encryption algorithm that provides strong security for encrypted data.

# Import the necessary modules from the cryptography library
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# User's input password
password = b"mysecretpassword"

# Generate a salt (random value used to prevent rainbow table attacks)
salt = b'\x85\x1cD\xa2\x14-\x08i\x04\x1d\xfb\xa5\xd7<2}'

# Generate a key using PBKDF2HMAC (Password-Based Key Derivation Function)
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    iterations=100000,
    salt=salt,
    length=32  # Length of the derived key
)
key = kdf.derive(password)

# Generate a random Fernet key
fernet_key = Fernet.generate_key()

# Create a Fernet cipher object with the generated key
cipher_suite = Fernet(fernet_key)

# Message to be encrypted
message = b"This is a secret message."

# Encrypt the message using the Fernet cipher
encrypted_message = cipher_suite.encrypt(message)

# Decrypt the encrypted message using the same Fernet cipher
decrypted_message = cipher_suite.decrypt(encrypted_message)

# Print the original message, encrypted message, and decrypted message
print(f"Original message: {message.decode('utf-8')}")
print(f"Encrypted message: {encrypted_message}")
print(f"Decrypted message: {decrypted_message.decode('utf-8')}")
