import re

def assess_password_strength(password):
    """
    Assess the strength of a given password.

    Args:
        password (str): The password to evaluate.

    Returns:
        dict: A dictionary containing the score, strength level, and feedback.
    """
    # Criteria checks
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_character_criteria = any(char in "!@#$%^&*()-_=+[{]}|;:'\",<.>/?`~" for char in password)

    # Scoring
    score = sum([
        length_criteria,
        uppercase_criteria,
        lowercase_criteria,
        digit_criteria,
        special_character_criteria
    ])

    # Feedback messages
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Include at least one lowercase letter.")
    if not digit_criteria:
        feedback.append("Include at least one numeric digit.")
    if not special_character_criteria:
        feedback.append("Include at least one special character (!@#$%^&* etc.).")

    # Determine strength level
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return {
        "score": score,
        "strength": strength,
        "feedback": feedback
    }

def main():
    """
    Main function to interact with the user and assess password strength.
    """
    print("Welcome to the Password Strength Assessment Tool!")
    while True:
        password = input("Enter a password to evaluate (or type 'exit' to quit): ")
        if password.lower() == "exit":
            print("Goodbye!")
            break

        result = assess_password_strength(password)
        print(f"\nPassword Strength: {result['strength']}")
        print("Feedback:")
        for msg in result["feedback"]:
            print(f" - {msg}")
        print("\n" + "-" * 40 + "\n")

if __name__ == "__main__":
    main()
