# 🎯 Number Guessing Game
# Code by Adiba | GitHub Portfolio

# The number to be guessed
secret_number = 36

# Start the guess count
attempts = 1

# Take the first guess
guess = int(input("🎲 Guess the number: "))

# Loop until the user guesses correctly
while guess != secret_number:
    if guess < secret_number:
        guess = int(input("🔻 Too low! Try again: "))
    else:
        guess = int(input("🔺 Too high! Try again: "))
    attempts += 1

# Print success message
print(f"🎉 You won in {attempts} attempts!")