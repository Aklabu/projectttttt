import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    characters = string.ascii_lowercase  # Start with lowercase letters

    # Add optional character sets
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    # Ensure the password contains at least one character from each selected set
    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_numbers:
        password.append(random.choice(string.digits))
    if use_special_chars:
        password.append(random.choice(string.punctuation))

    # Fill the rest of the password length with random characters
    while len(password) < length:
        password.append(random.choice(characters))

    # Shuffle the password list and join it to form the final password
    random.shuffle(password)
    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    
    # Get user preferences
    length = int(input("Enter the desired password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    
    # Generate password
    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
    
    print(f"\nYour generated password is: {password}")

if __name__ == "__main__":
    main()
