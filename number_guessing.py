import random

def guess_num():
    # Generate a random number between 1 and 100
    secret_num = random.randint(1, 100)
    attempts = 0

    # Welcome message and instructions
    print("Number Guessing game!")
    print("There's a secret a number between 0 and 100. Can you guess it in as few tries as possible?")

    while True:
        try:
            # Prompt the player to enter their guess
            guess = int(input("Enter your guess: "))
        except ValueError:
            # Handle non-integer input
            print("That ain't a number. Enter a valid NUMBER.")
            continue

        attempts += 1

        if guess == secret_num:
            # Player guessed the correct number
            print(f"Congrats! You got it in {attempts} attempt(s).")
            break
        elif guess < secret_num:
            # Player's guess is lower than the secret number
            print("Nah, too low. Try again.")
        else:
            # Player's guess is higher than the secret number
            print("Nope, too high. Try again.")

if __name__ == "__main__":
    guess_num()