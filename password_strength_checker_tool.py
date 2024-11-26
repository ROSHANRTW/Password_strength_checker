import re
import os


# Styling using ANSI escape codes for colors
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    BLUE = '\033[94m'


def check_password_strength(password):
    """
    Function to evaluate password strength.
    Returns a strength score and a message.
    """
    strength_score = 0
    criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r'[A-Z]', password)),
        "lowercase": bool(re.search(r'[a-z]', password)),
        "digits": bool(re.search(r'\d', password)),
        "special": bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)),
        "no_spaces": not bool(re.search(r'\s', password))
    }

    # Check each criterion
    for criterion, passed in criteria.items():
        if passed:
            strength_score += 1

    # Determine strength level
    if strength_score == 6:
        return strength_score, "Very Strong"
    elif 4 <= strength_score < 6:
        return strength_score, "Strong"
    elif 3 <= strength_score < 4:
        return strength_score, "Moderate"
    else:
        return strength_score, "Weak"


def reset_screen():
    """Function to clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    while True:
        reset_screen()
        print(f"{Colors.RED}Hello ITS CREATED BY CyberRoshan")
        print(f"{Colors.BOLD}{Colors.BLUE}Welcome to the Password Strength Checker Tool!{Colors.RESET}")
        print(f"{Colors.CYAN}Evaluate your password strength and get tips to improve it.{Colors.RESET}")
        print("\nOptions:")
        print(f"1. Check password strength")
        print(f"2. Reset screen")
        print(f"3. Exit\n")

        choice = input("Choose an option (1/2/3): ")
        if choice == "1":
            password = input("\nEnter a password to check its strength: ")
            score, strength = check_password_strength(password)

            # Show the result with color
            if strength == "Very Strong":
                color = Colors.GREEN
            elif strength == "Strong":
                color = Colors.YELLOW
            elif strength == "Moderate":
                color = Colors.BLUE
            else:
                color = Colors.RED

            print(f"\nPassword Strength: {color}{strength}{Colors.RESET} (Score: {score}/6)")

            # Provide feedback
            if score < 6:
                print(f"{Colors.BOLD}\nSuggestions to improve your password:{Colors.RESET}")
                if len(password) < 8:
                    print(f"- {Colors.RED}Make your password at least 8 characters long.{Colors.RESET}")
                if not re.search(r'[A-Z]', password):
                    print(f"- {Colors.RED}Add at least one uppercase letter.{Colors.RESET}")
                if not re.search(r'[a-z]', password):
                    print(f"- {Colors.RED}Add at least one lowercase letter.{Colors.RESET}")
                if not re.search(r'\d', password):
                    print(f"- {Colors.RED}Include at least one digit.{Colors.RESET}")
                if not re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
                    print(f"- {Colors.RED}Add at least one special character.{Colors.RESET}")
                if re.search(r'\s', password):
                    print(f"- {Colors.RED}Avoid using spaces in your password.{Colors.RESET}")
            else:
                print(f"{Colors.GREEN}\nGreat job! Your password is strong.{Colors.RESET}")

            input("\nPress Enter to return to the main menu.")

        elif choice == "2":
            reset_screen()
            print(f"{Colors.CYAN}Screen has been reset. Returning to the main menu...{Colors.RESET}")
        elif choice == "3":
            print(f"{Colors.YELLOW}Exiting the tool. Stay safe and create strong passwords!{Colors.RESET}")
            break
        else:
            print(f"{Colors.RED}Invalid choice. Please select 1, 2, or 3.{Colors.RESET}")
            input("Press Enter to try again.")


if __name__ == "__main__":
    main()
