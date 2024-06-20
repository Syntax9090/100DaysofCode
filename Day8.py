# Advanced Cute Message Displayer for GitHub Enthusiasts

# Function to display a message based on the user's choice
def display_message(choice, user_name):
    messages = {
        1: f"{user_name}, you're a code wizard! 🧙‍♂️",
        2: f"{user_name}, your repositories are legendary! 🚀",
        3: f"{user_name}, your commits are pure gold! ✨",
        4: f"{user_name}, your pull requests make the world better! 🌟",
        5: f"{user_name}, you're a GitHub superstar! ⭐"
    }
    
    # Retrieve and display the message based on user choice
    return messages.get(choice, "Invalid choice. Please enter a number between 1 and 5.")

# Main program function
def main():
    print("Welcome to the GitHub Enthusiast Message Displayer!")
    user_name = input("Please enter your GitHub username: ")
    
    while True:
        # Print the menu options for the user
        print("\nMenu:")
        print("1: Code Wizard Message")
        print("2: Legendary Repositories Message")
        print("3: Gold Commit Message")
        print("4: Awesome Pull Request Message")
        print("5: Superstar Message")
        print("0: Exit")

        try:
            # Get the user's choice as an integer
            choice = int(input("Enter the number of your choice (or 0 to exit): "))
            
            if choice == 0:
                print("Goodbye! Keep coding and contributing on GitHub!")
                break
            
            # Display the message based on the user's choice
            print(display_message(choice, user_name))
        
        except ValueError:
            # Handle the case where the user input is not an integer
            print("Invalid input! Please enter a number between 0 and 5.")

# Run the main program if this script is executed (not imported as a module)
if __name__ == "__main__":
    main()
