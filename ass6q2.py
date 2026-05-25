import random

options = ["rock", "paper", "scissors"]
rounds = 0
user_score = 0
computer_score = 0


while True:
    print(f"*****Round {rounds + 1}*****")
    user_choice = input("Enter your choice (rock, paper, scissors) or 'exit' to quit: ").lower()
    print(f"You chose: {user_choice}")


    if user_choice == "exit":
        print("Thanks for playing!")
        print(f"Final Score - You: {user_score}, Computer: {computer_score}")
        break
    if user_choice not in options:
        print("Invalid choice. Please try again.")
        continue

    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")


    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        user_score += 1
    else:
        computer_score += 1
    print(f"Current Score - You: {user_score}, Computer: {computer_score}\n")
    rounds += 1

if user_score > computer_score:
    print("Congratulations! You won the game!")
elif user_score < computer_score:
    print("Sorry! The computer won the game!")
else:
    print("It's a draw!")