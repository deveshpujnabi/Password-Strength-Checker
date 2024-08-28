import re

def password_strength(password):
    """
    Evaluates the strength of a password.
    A message indicating the password strength (weak, medium, strong).
    """
    strength = 'weak'

    # Check password length
    if len(password) < 8:
        return 'weak'

    # Check for digits
    if re.search(r'\d', password):
        strength = 'medium'

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength = 'medium'

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength = 'medium'

    # Check for special characters
    if re.search(r'[^A-Za-z0-9]', password):
        strength = 'strong'

    return strength

# Example usage
password = input("Enter a password: ")
print("Password strength:", password_strength(password))