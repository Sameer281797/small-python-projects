# Python Quiz Game

questions = (
    "How many elements are there in the periodic table?",
    "Which animal lays the largest egg?",
    "What is the most abundant gas in Earth's atmosphere?",
    "How many bones are in the human body?",
    "Which planet in the solar system is the hottest?"
)

options = (
    ("A. 116", "B. 117", "C. 118", "D. 119"),
    ("A. WHALE", "B. CROCODILE", "C. ELEPHANT", "D. OSTRICH"),
    ("A. NITROGEN", "B. O2", "C. CO2", "D. HYDROGEN"),
    ("A. 206", "B. 207", "C. 208", "D. 209"),
    ("A. MERCURY", "B. VENUS", "C. EARTH", "D. MARS")
)

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0

for i in range(len(questions)):
    print("---------------------------")
    print(questions[i])
    for option in options[i]:
        print(option)
    
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[i]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[i]} is the correct answer!")

print("---------------------------")
print("RESULTS")
print("---------------------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score_percent = int(score / len(questions) * 100)
print(f"\nYour score is: {score_percent}%")

            