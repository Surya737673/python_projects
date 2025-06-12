import random

secret_number = random.randint(1, 100)

print("Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Please enter a valid number.")
        continue

    if guess == secret_number:
        print("Congratulations! You guessed the number!")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")