import random

print("🎯 Guess the Number Game (1 - 10)")

while True:
    randnumber = random.randint(1, 10)
    userguess = None
    guesses = 0

    while userguess != randnumber:
        try:
            userguess = int(input("Enter your guess: "))
            guesses += 1

            if userguess == randnumber:
                print("🎉 You guessed it right!")
                print(f"🔢 Total guesses: {guesses}")
            elif userguess > randnumber:
                print("❌ Too high! Try a smaller number.")
            else:
                print("❌ Too low! Try a larger number.")
        except ValueError:
            print("⚠️ Invalid input! Please enter a number between 1 and 10.")

    newgame = input("Do you want to play again? (yes/no): ").lower()
    if newgame != 'yes':
        print("👋 Thanks for playing!")
        break
