# The Diffie-Hellman key exchange is a groundbreaking cryptographic protocol that enables
# secure key exchange over an untrusted communication channel.
# Invented by Whitfield Diffie and Martin Hellman in 1976.

from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

# Generate common Diffie-Hellman parameters for both Alice and Bob
parameters = dh.generate_parameters(generator=2, key_size=2048)

# Generate private and public keys for Alice
private_key_alice = parameters.generate_private_key()
public_key_alice = private_key_alice.public_key()

# Generate private and public keys for Bob
private_key_bob = parameters.generate_private_key()
public_key_bob = private_key_bob.public_key()

# Perform the key exchange
shared_key_alice = private_key_alice.exchange(public_key_bob)
shared_key_bob = private_key_bob.exchange(public_key_alice)

# Print the shared keys
print(f"Alice's shared key: {shared_key_alice.hex()}")
print(f"Bob's shared key: {shared_key_bob.hex()}")
