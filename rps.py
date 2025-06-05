import random

user_choice = input("Choose rock, paper, or scissors: ").lower()
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
print(f"Computer chose: {computer_choice}")
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
elif (computer_choice == "rock" and user_choice == "scissors") or \
     (computer_choice == "paper" and user_choice == "rock") or \
     (computer_choice == "scissors" and user_choice == "paper"):
    print("You lose!")
else: 

    print("Invalid choice. Please choose rock, paper, or scissors.")
# This code implements a simple Rock, Paper, Scissors game.
# The user inputs their choice, and the computer randomly selects one.