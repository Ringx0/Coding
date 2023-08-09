import random
import time

# Welcome message for the guessing game.
print("Welcome to the guessing game. I am going to pick a number between 1 and 100")

# Pause for 3 seconds to build anticipation.
time.sleep(3)

# Inform the user that the program is "picking" a number.
print("Picking a number...")

# Pause for 2 seconds to simulate the selection process.
time.sleep(2)

# Get the user's initial guess as an integer input.
guess = int(input("What is your guess?: "))

# Generate a random number between 1 and 100 as the correct number to guess.
correct_number = random.randint(1, 100)

# Initialize a counter for the number of guesses made.
guess_count = 1

# Start a loop that continues until the guess matches the correct number.
while guess != correct_number:
    # Pause for 1 second before prompting for the next guess.
    time.sleep(1)
    
    # Increment the guess count for each iteration.
    guess_count += 1
    
    # Check if the guess is lower or higher than the correct number and provide guidance.
    if guess < correct_number:
        guess = int(input("Wrong. You need to guess higher. What is your guess?: "))
    else:
        guess = int(input("Wrong. You need to guess lower. What is your guess?: "))

# Pause for 1 second before displaying the final result.
time.sleep(1)

# Display a congratulatory message along with the correct number and the number of guesses made.
print(f"Congrats! The right answer was {correct_number}. It took you {guess_count} guesses.")
