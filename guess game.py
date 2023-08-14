import random

# Generate a random number for the first player
min_num = 1
max_num = 100
target_number = random.randint(min_num, max_num)

print("First player, a random number has been generated. Second player, start guessing!")

# Second player guesses the number
attempts = 0
while True:
    guess = int(input("Second player, enter your guess: "))
    attempts += 1

    if guess == target_number:
        print(f"Congratulations! Second player guessed the correct number {target_number} in {attempts} attempts.")
        break
    elif guess < target_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
