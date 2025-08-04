# 🎯 Number Guessing Game (Random Version)
# Code by Adiba | GitHub Portfolio

import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Start the guess count
attempts = 1

# Take the first guess
guess = int(input("🎲 Guess the number (between 1 and 100): "))

# Loop until the user guesses correctly
while guess != secret_number:
    if guess < secret_number:
        guess = int(input("🔻 Too low! Try again: "))
    else:
        guess = int(input("🔺 Too high! Try again: "))
    attempts += 1

# Print success message
print(f"🎉 You won in {attempts} attempts! The number was {secret_number}.")