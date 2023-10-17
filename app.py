# Import the 'secrets' module for secure random number generation
import secrets

# Import the 'string' module to access string constants like letters, digits, and special characters
import string

# Define a function 'create_pw' that generates a strong password
def create_pw(pw_length=8):
    # Define character sets for uppercase and lowercase letters, digits, and special characters
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    # Combine all character sets to form the complete alphabet for password generation
    alphabet = letters + digits + special_chars
    pwd = ''  # Initialize an empty string to store the password
    pw_strong = False  # Initialize a flag to track if the password meets the strength criteria

    # Loop until a strong password is generated
    while not pw_strong:
        # Generate a password of specified length by choosing characters randomly from the alphabet
        pwd = ''.join(secrets.choice(alphabet) for _ in range(pw_length))

        # Check if the password contains at least one special character and at least two digits
        if any(char in special_chars for char in pwd) and sum(char in digits for char in pwd) >= 2:
            pw_strong = True  # Password meets the strength criteria, set the flag to True

    return pwd  # Return the generated strong password

# Entry point of the script
if __name__ == '__main__':
    # Print the generated strong password using the 'create_pw' function
    print("Generated Password:", create_pw())
