import random

# Computer choice
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)

# User input
user_choice = input("Enter your choice (Rock, Paper, Scissors): ").lower()

# Display choices
print(f"Computer chose: {computer_choice.capitalize()}")
print(f"You chose: {user_choice.capitalize()}")

# Determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("You win!")
    else:
        print("Computer wins!")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("You win!")
    else:
        print("Computer wins!")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("You win!")
    else:
        print("Computer wins!")
else:
    print("Invalid choice. Please choose Rock, Paper, or Scissors.")
