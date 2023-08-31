# A hash function takes an input and produces a fixed-size string
# of characters (hash value). It's commonly used for data integrity verification,
# password storage, digital signatures, and more.

# Definition of a hash function:
# - Takes an input (message)
# - Produces a fixed-size output (hash value)
# - Deterministic (same input always produces the same hash)
# - Efficient to compute
# - Pre-image resistance (hard to find input given the hash)
# - Collision resistance (hard to find two inputs with the same hash)

#  About SHA-256:
# - Part of SHA-2 family, widely used for security purposes
# - Produces a 256-bit (32-byte) hash value
# - Used in Bitcoin's blockchain for block hashing, transaction signing, etc.
# - Provides strong collision resistance and pre-image resistance
# - Secure for various cryptographic applications


import hashlib


def sha256_hash(data):
    # Create a hashlib object for SHA-256
    sha256 = hashlib.sha256()

    # Update the hashlib object with the input data, encoded as UTF-8
    sha256.update(data.encode('utf-8'))

    # Get the hexadecimal representation of the hash value
    return sha256.hexdigest()


# Input data
input_data = "Hello, this is a demonstration of SHA-256 hashing!"

# Calculate the SHA-256 hash
hash_value = sha256_hash(input_data)

# Print the input data and its SHA-256 hash
print("Input Data:", input_data)
print("SHA-256 Hash:", hash_value)
