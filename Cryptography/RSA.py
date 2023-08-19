# RSA (Rivest-Shamir-Adleman) is a widely used asymmetric encryption algorithm.
# It was invented in 1977 and is unique due to its reliance on the difficulty of factoring large composite numbers.

# Import necessary modules from the cryptography library
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

# Generate an RSA key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,  # A common value for the public exponent
    key_size=2048  # Key size in bits
)

# Serialize the private key in PEM format
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()  # No passphrase for encryption
)

# Extract the public key from the private key
public_key = private_key.public_key()

# Message to be encrypted
message = b"Hello, this is a secret message!"

# Encrypt the message using the public key and OAEP padding
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),  # Mask Generation Function
        algorithm=hashes.SHA256(),  # Hashing algorithm
        label=None  # Optional label (usually set to None)
    )
)

# Decrypt the encrypted message using the private key and OAEP padding
decrypted_message = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),  # Mask Generation Function
        algorithm=hashes.SHA256(),  # Hashing algorithm
        label=None  # Optional label (usually set to None)
    )
)

# Print the original message, encrypted message, and decrypted message
print(f"Original message: {message.decode('utf-8')}")
print(f"Encrypted message: {ciphertext}")  # Print the encrypted message
print(f"Decrypted message: {decrypted_message.decode('utf-8')}")
