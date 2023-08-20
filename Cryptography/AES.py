# AES (Advanced Encryption Standard) is a widely used symmetric encryption algorithm.
# It was established as a standard by NIST (National Institute of Standards and Technology) in 2001.

# Import the necessary module from the cryptography library
from cryptography.fernet import Fernet

# Generate a random symmetric key
key = Fernet.generate_key()

# Create a Fernet cipher object with the generated key
cipher_suite = Fernet(key)

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
