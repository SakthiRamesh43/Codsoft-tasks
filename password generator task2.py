#---password generato---
import random
import string

def generate_password(length):
    if length < 4:  # Ensure the password length
        print("Password length should be at least 4.")
        return None

    # Define character sets for password generation
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure the password has at least one character from each set
    all_characters = lower + upper + digits + symbols
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the remaining length with random choices from all characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password
    random.shuffle(password)

    return ''.join(password)

# Get user input for password lengthj
try:
    length = int(input("Enter the desired length of the password: "))
    password = generate_password(length)
    if password:
        print(f"Generated Password: {password}")
except ValueError:
    print("Please enter a valid integer for the password length.")