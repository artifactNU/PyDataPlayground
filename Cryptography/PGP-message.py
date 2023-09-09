import gnupg

# Example paths to key files
recipient_public_key = "C:/path/to/recipient_public_key.asc"

# Uncomment the following code if you want to sign the message:
"""
your_private_key = "C:/path/to/your_private_key.asc"
"""

# Message to be encrypted and signed
message = "A secret message."

# Initialize GPG instance
gpg = gnupg.GPG()

# Load recipient's public key
with open(recipient_public_key, "r") as file:
    recipient_key_data = file.read()

# Load your private key
# Uncomment the following code if you want to sign the message:
"""
with open(your_private_key, "r") as file:
    your_key_data = file.read()
"""

# Encrypt the message
encrypted_message = gpg.encrypt(message, recipient_key_data)

if encrypted_message.ok:
    encrypted_data = str(encrypted_message)
    print("Encrypted Message:")
    print(encrypted_data)
else:
    print("Encryption failed.")
    print(encrypted_message.status)

# Uncomment the following code if you want to sign the message:
"""
# Sign the message
signed_message = gpg.sign(encrypted_data, key_data=your_key_data, passphrase="yourpassphrase")

if signed_message.ok:
    signed_data = str(signed_message)
    print("Signed Message:")
    print(signed_data)
else:
    print("Signing failed.")
    print(signed_message.status)
"""
