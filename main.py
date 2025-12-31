import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Initialize variables
guess = 0
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 10.")

# Keep asking until the correct number is guessed
while guess != secret_number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
    else:
        print(f"Correct! You guessed the number in {attempts} attempts.")
