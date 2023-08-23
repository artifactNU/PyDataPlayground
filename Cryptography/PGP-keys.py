import gnupg

# Define your credentials
name = "Your Name"  # Change to your name
email = "your.email@example.com"  # Change to your email
passphrase = "yourpassphrase"  # Change to your passphrase

# Function to generate a PGP key pair
def generate_key_pair():
    gpg = gnupg.GPG()
    input_data = gpg.gen_key_input(
        name_real=name,
        name_email=email,
        passphrase=passphrase,
        key_type="RSA",
        key_length=2048,
        subkey_type="RSA",
        subkey_length=2048
    )
    key = gpg.gen_key(input_data)
    return key

if __name__ == "__main__":
    gpg = gnupg.GPG()  # Create a GPG instance
    key = generate_key_pair()

    # Save private key to a text file
    private_key_file = "private_key.asc"
    with open(private_key_file, "w") as file:
        file.write(str(key))

    # Export and save public key to a text file
    public_key_file = "public_key.asc"
    with open(public_key_file, "w") as file:
        file.write(gpg.export_keys(key.fingerprint))

    # Save fingerprint to a text file
    fingerprint_file = "fingerprint.txt"
    with open(fingerprint_file, "w") as file:
        file.write(key.fingerprint)

    print("Generated key pair with fingerprint:", key.fingerprint)
    print("Private key saved to:", private_key_file)
    print("Public key saved to:", public_key_file)
    print("Fingerprint saved to:", fingerprint_file)
