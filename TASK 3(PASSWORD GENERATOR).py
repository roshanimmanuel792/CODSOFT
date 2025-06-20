import random
import string

def generate_password(length):
    """Generate a random password of specified length."""
    # Define character set (letters, numbers, and symbols)
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    """Main function to run the password generator."""
    print("=== Password Generator ===")
    
    # Get password length from user
    while True:
        try:
            length = int(input("Enter desired password length: "))
            if length > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Generate and display password
    password = generate_password(length)
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()