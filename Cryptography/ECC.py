# Elliptic Curve Cryptography (ECC) is a powerful cryptographic scheme that relies on the mathematics of elliptic curves
# over finite fields to provide strong security with relatively small key sizes. ECC was first proposed by Neal Koblitz and
# Victor S. Miller independently in the mid-1980s.

# Import the necessary modules from the cryptography library
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes

# Generate Alice's ECC private key and corresponding public key
private_key_alice = ec.generate_private_key(ec.SECP256R1())
public_key_alice = private_key_alice.public_key()

# Generate Bob's ECC private key and corresponding public key
private_key_bob = ec.generate_private_key(ec.SECP256R1())
public_key_bob = private_key_bob.public_key()

# Perform ECC-based key exchange
shared_secret_alice = private_key_alice.exchange(ec.ECDH(), public_key_bob)
shared_secret_bob = private_key_bob.exchange(ec.ECDH(), public_key_alice)

# Verify that the shared secrets match
assert shared_secret_alice == shared_secret_bob

# Sign a message using Alice's private key
message = b"This is a message to be signed."
signature = private_key_alice.sign(message, ec.ECDSA(hashes.SHA256()))

# Verify the signature using Alice's public key
try:
    public_key_alice.verify(signature, message, ec.ECDSA(hashes.SHA256()))
    print("Signature verified successfully.")
    print("Original message:", message.decode('utf-8'))
except Exception as e:
    print("Signature verification failed:", str(e))