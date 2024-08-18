import re

def assess_password_strength(password):
    # Initialize strength level
    strength = 0
    feedback = []

    # Length criterion
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase letters criterion
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter (A-Z).")

    # Lowercase letters criterion
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter (a-z).")

    # Numbers criterion
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one digit (0-9).")

    # Special characters criterion
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character (e.g., !, @, #, $).")

    # Evaluate overall strength
    if strength == 5:
        feedback.append("Your password is strong.")
    elif 3 <= strength < 5:
        feedback.append("Your password is moderate. Consider adding more complexity.")
    else:
        feedback.append("Your password is weak. It needs significant improvement.")

    return feedback

def main():
    print("Password Strength Assessment Tool")
    password = input("Enter a password to assess: ").strip()
    
    feedback = assess_password_strength(password)
    
    print("\nPassword Strength Feedback:")
    for line in feedback:
        print(f"- {line}")

if __name__ == "__main__":
    main()
