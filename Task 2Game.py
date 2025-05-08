import random

# Function to start the guessing game
def guess_number():
    # Random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    # Variable to track the number of attempts
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Loop until the user guesses the number
    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check if the guess is correct, too high, or too low
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the correct number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

# Start the game
guess_number()
