import random
print("\n" + "=" * 30)
print("       ROCK PAPER SCISSORS")
print("=" * 30)

choices = ["Rock", "Paper", "Scissors"]

while True:

    print("\nChoose your option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    try:
        choice = int(input("\nEnter your choice (1-3): "))

        if choice < 1 or choice > 3:
            print("Invalid choice!")
            continue

        user_choice = choices[choice - 1]
        computer_choice = random.choice(choices)

        print("\nYou chose     :", user_choice)
        print("Computer chose:", computer_choice)

        if user_choice == computer_choice:
            print("\nResult: It's a Draw!")

        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            print("\nResult: You Win!")

        else:
            print("\nResult: Computer Wins!")

        again = input("\nDo you want to play again? (yes/no): ")

        if again.lower() == "no":
            print("\nThank you for playing!")
            break

    except ValueError:
        print("Please enter a valid number.")