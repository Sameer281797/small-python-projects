import random

def playgame():
    choices = ['snake', 'water', 'gun']

    while True:
        your_choice = input("Enter your choice (snake, water, gun): ").lower()
        if your_choice not in choices:
            print("Invalid input. Please enter snake, water, or gun.")
            continue

        computer_choice = random.choice(choices)
        print("Computer's choice:", computer_choice)

        if your_choice == computer_choice:
            print("It's a tie!")
        elif (
            (your_choice == 'snake' and computer_choice == 'water') or
            (your_choice == 'water' and computer_choice == 'gun') or
            (your_choice == 'gun' and computer_choice == 'snake')
        ):
            print("You win!")
        else:
            print("You lose!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    print("🐍 Welcome to the Snake, Water, Gun Game! 🔫")
    playgame()
