import re

def assess_password_strength(password):

    feedback = {}
    
    # Check password length
    if len(password) < 8:
        feedback['Length'] = "Weak: Password should be at least 8 characters long"
    elif len(password) <= 12:
        feedback['Length'] = "Moderate: Consider increasing the length for better security"
    else:
        feedback['Length'] = "Strong: Good length ✔"

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        feedback['Uppercase'] = "Contains uppercase letters ✔"
    else:
        feedback['Uppercase'] = "Weak: Include at least one uppercase letter."

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        feedback['Lowercase'] = "Contains lowercase letters ✔"
    else:
        feedback['Lowercase'] = "Weak: Include at least one lowercase letter"

    # Check for numbers
    if re.search(r'[0-9]', password):
        feedback['Numbers'] = "Contains numbers ✔"
    else:
        feedback['Numbers'] = "Weak: Include at least one number"

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        feedback['Special Characters'] = "Contains special characters ✔"
    else:
        feedback['Special Characters'] = "Weak: Include at least one special character"

    # Overall strength
    if all(value.startswith('Contains') or value.startswith('Strong') for value in feedback.values()):
        feedback['Overall'] = "Strong: Your password is secure ✔"
    else:
        feedback['Overall'] = "Weak: Your password could be improved"

    return feedback

def print_feedback(feedback):
   
    print("\nPassword Strength Assessment:")
    for criterion, message in feedback.items():
        print(f"{criterion}: {message}")

# Example usage
password = input("Enter a password to assess: ")
feedback = assess_password_strength(password)
print_feedback(feedback)
