Advanced Password Generator : 
An advanced password generator designed to create secure, customizable passwords with specific complexity requirements. It includes options to set password length, minimum counts of digits, uppercase, lowercase, symbols, and an option to specify custom symbols. Additionally, it checks password strength and saves the generated password with an expiry date.

Features : 
Customizable Length: Choose a desired password length.
Complexity Requirements: Set minimum counts for digits, uppercase, lowercase, and symbols.
Strength Checker: Checks and categorizes password strength as Weak, Moderate, or Strong.
Custom Symbols: Option to include specific symbols as per your requirements.
Expiry Date: Saves the generated password with an expiration date in passwords.txt.

Getting Started : 
Prerequisites : 
Python 3.x

Usage : 
Run the script to generate a password:

bash:
python password_generator.py

Follow the prompts to enter your requirements for password length and complexity.

Example : 
plaintext : 

Welcome to the Advanced Password Generator!
Enter the desired password length (minimum 12): 16
Enter the minimum number of digits (minimum 1): 2
Enter the minimum number of uppercase letters (minimum 1): 2
Enter the minimum number of lowercase letters (minimum 1): 2
Enter the minimum number of symbols (minimum 1): 2
Enter custom symbols to include in password (leave empty for default): @#$

Your generated password is: 9W@sD4h!eR2Q
Password strength: Strong
Enter the number of days until password expiry: 30
Password saved with expiry date: 2024-11-27

Files : 
password_generator.py: Main script to generate and manage passwords.
passwords.txt: Stores generated passwords along with their expiry dates.

License : 
This project is licensed under the MIT License. See LICENSE for more details.

https://github.com/SoaibAslam/Random_Password_Generator/blob/main/Random%20Password%20Generator.py