# version2_guess_game_menu_driven.py
import random

def choose_level():
    print("\nChoose difficulty level:")
    print("1. Easy   (Range: 1–10   | Attempts: 5)")
    print("2. Medium (Range: 1–50   | Attempts: 7)")
    print("3. Hard   (Range: 1–100  | Attempts: 10)")

    while True:
        choice = input("Enter 1, 2, or 3: ").strip()

        if choice == "1":
            return 1, 10, 5
        elif choice == "2":
            return 1, 50, 7
        elif choice == "3":
            return 1, 100, 10
        else:
            print("❌ Invalid choice. Try again.")

def give_hint(guess, number):
    difference = abs(guess - number)

    if difference == 0:
        return "🎯 Exact match!"

    if difference <= 3:
        return "🔥 Very Hot!"
    elif difference <= 7:
        return "🌡 Warm"
    else:
        return "❄ Cold"

def how_to_play():
    print("""
=== HOW TO PLAY ===

1. Choose a difficulty level.
2. Enter guesses to find the secret number.
3. Clues will help you:
   - HOT / WARM / COLD clue (based on closeness)
   - GO HIGHER / GO LOWER hint
4. Don't run out of attempts.

""")

def play():
    start, end, attempts = choose_level()
    number = random.randint(start, end)

    print(f"\nI'm thinking of a number between {start} and {end}.")
    print(f"You have {attempts} attempts.\n")

    while attempts > 0:
        guess = input("Your guess: ").strip()

        if not guess.isdigit():
            print("❌ Enter a valid number.\n")
            continue

        guess = int(guess)
        attempts -= 1

        if guess == number:
            print(f"✅ Correct! The number was {number}.")
            break

        print(give_hint(guess, number))
        print("   ➤ Go Higher!" if guess < number else "   ➤ Go Lower!")
        print(f"Attempts left: {attempts}\n")

    if attempts == 0:
        print(f"❌ You're out of attempts! The correct number was {number}.")

def menu():
    while True:
        print("\n=== NUMBER GUESSING GAME MENU ===")
        print("1. Play Game")
        print("2. How to Play")
        print("3. Exit")

        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            play()
            while True:
                again = input("\nPlay again? (y/n): ").strip().lower()
                if again == "y":
                    play()
                elif again == "n":
                    break
                else:
                    print("Enter only y or n.")
        elif choice == "2":
            how_to_play()
        elif choice == "3":
            print("👋 Thanks for playing!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    menu()