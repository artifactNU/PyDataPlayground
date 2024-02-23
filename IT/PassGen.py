import secrets
import string

def generate_password(length=12):
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a secure random password of specified length
    password = ''.join(secrets.choice(characters) for _ in range(length))
    
    return password

def main():
    # Prompt user to input password length
    length = int(input("Enter the length of the password: "))
    
    # Generate password
    password = generate_password(length)
    
    # Print the generated password
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
