# simple_guess.py
import random

def play():
    number = random.randint(1, 50)
    print("I'm thinking of a number between 1 and 50. Try to guess it!")
    while True:
        guess = input("Your guess: ").strip()
        if not guess.isdigit():
            print("Please enter a valid integer.")
            continue
        guess = int(guess)
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Correct! The number was {number}.")
            break

if __name__ == "__main__":
    play()