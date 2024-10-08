import random
import string
import re
from datetime import datetime, timedelta

# Constants for password complexity
DEFAULT_LENGTH = 12
MIN_DIGITS = 1
MIN_UPPERCASE = 1
MIN_LOWERCASE = 1
MIN_SYMBOLS = 1

def generate_password(length, min_digits, min_uppercase, min_lowercase, min_symbols, custom_symbols):
    if length < (min_digits + min_uppercase + min_lowercase + min_symbols):
        raise ValueError("Password length is too short for the given complexity requirements.")
    
    # Define character sets
    digits = string.digits
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    symbols = custom_symbols if custom_symbols else string.punctuation
    
    # Ensure the minimum requirements are met
    password = [
        random.choice(digits) for _ in range(min_digits)
    ] + [
        random.choice(uppercase) for _ in range(min_uppercase)
    ] + [
        random.choice(lowercase) for _ in range(min_lowercase)
    ] + [
        random.choice(symbols) for _ in range(min_symbols)
    ]
    
    # Fill the remaining length with a random selection from all character sets
    all_characters = digits + uppercase + lowercase + symbols
    remaining_length = length - len(password)
    password += [random.choice(all_characters) for _ in range(remaining_length)]
    
    # Shuffle to ensure randomness
    random.shuffle(password)
    
    return ''.join(password)

def check_password_strength(password):
    """ Check the strength of the password """
    length = len(password)
    if length < 8:
        return "Weak"
    elif re.search(r'[A-Z]', password) and re.search(r'[a-z]', password) and re.search(r'[0-9]', password) and re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Strong"
    else:
        return "Moderate"

def save_password_to_file(password, expiry_date):
    """ Save the password and its expiry date to a file """
    with open('passwords.txt', 'a') as file:
        file.write(f"Password: {password}\nExpiry Date: {expiry_date}\n\n")

def main():
    # User input for password requirements
    print("Welcome to the Advanced Password Generator!")
    length = int(input(f"Enter the desired password length (minimum {DEFAULT_LENGTH}): ") or DEFAULT_LENGTH)
    min_digits = int(input(f"Enter the minimum number of digits (minimum {MIN_DIGITS}): ") or MIN_DIGITS)
    min_uppercase = int(input(f"Enter the minimum number of uppercase letters (minimum {MIN_UPPERCASE}): ") or MIN_UPPERCASE)
    min_lowercase = int(input(f"Enter the minimum number of lowercase letters (minimum {MIN_LOWERCASE}): ") or MIN_LOWERCASE)
    min_symbols = int(input(f"Enter the minimum number of symbols (minimum {MIN_SYMBOLS}): ") or MIN_SYMBOLS)
    custom_symbols = input("Enter custom symbols to include in password (leave empty for default): ")

    # Password generation
    try:
        password = generate_password(length, min_digits, min_uppercase, min_lowercase, min_symbols, custom_symbols)
        strength = check_password_strength(password)
        print(f"Your generated password is: {password}")
        print(f"Password strength: {strength}")

        # Save password to file
        expiry_days = int(input("Enter the number of days until password expiry: ") or 30)
        expiry_date = (datetime.now() + timedelta(days=expiry_days)).strftime('%Y-%m-%d')
        save_password_to_file(password, expiry_date)
        print(f"Password saved with expiry date: {expiry_date}")

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
