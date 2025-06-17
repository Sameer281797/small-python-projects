import random

print("🎰 Welcome to the Betting Game!")

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10
ROWS = 3
COLS = 3

symbol_count = {
    "A": 1,
    "B": 1,
    "C": 5,
}

symbol_values = {
    "A": 2,
    "B": 2,
    "C": 2,
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            if column[line] != symbol:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            end_char = " | " if i != len(columns) - 1 else ""
            print(column[row], end=end_char)
        print()

def deposit():
    while True:
        amount = input("What would you like to deposit? INR ₹:")
        if amount.isdigit():
            amount = int(amount)
            if amount >= MIN_BET:
                return amount
            else:
                print(f"Minimum deposit must be INR ₹{MIN_BET}")
        else:
            print("Please enter a valid number.")

def get_number_of_lines():
    while True:
        lines = input(f"Enter number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print("Invalid number of lines.")
        else:
            print("Please enter a valid number.")

def get_bet():
    while True:
        bet = input(f"What would you like to bet per line? INR ₹:")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                return bet
            else:
                print(f"Bet must be between ₹{MIN_BET} and ₹{MAX_BET}")
        else:
            print("Please enter a valid number.")

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Not enough balance. You have: ₹{balance}")
        else:
            break

    print(f"Betting ₹{bet} on {lines} line(s). Total bet: ₹{total_bet}")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"You won: ₹{winnings}")
    if winning_lines:
        print("Winning line(s):", ', '.join(map(str, winning_lines)))
    else:
        print("No winning lines.")

    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"\nCurrent balance: ₹{balance}")
        if balance < MIN_BET:
            choice = input("Low balance. Deposit more or press 'q' to quit: ").lower()
            if choice == 'q':
                break
            else:
                balance += deposit()
        else:
            action = input("Press Enter to spin or 'q' to quit: ").lower()
            if action == 'q':
                break
            balance += spin(balance)

    print(f"You left with ₹{balance}. Thanks for playing!")

main()
