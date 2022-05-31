#Number Guessing Game Objectives:

# Include an ASCII art logo.
from art import logo 
print(logo)
print("I'm thinking of a number between 1 and 100")

#Create a Random number will be used for comparering with user input
import random
random_number = random.randint(1,100)
print(random_number)

#Function to get user to pick difficulty 
def difficulty():
    user_input = input("Choose a dificulty: Type 'easy' or 'hard': ")
    if user_input == "easy":
        attempts = 10
        return attempts
    else:
        attempts = 5
        return attempts

# Allow the player to submit a guess for a number between 1 and 100.
def guess():
    user_guess = int(input("Make a guess: "))
    return user_guess
    
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
def compare(user_guess, random_number):
    # If they got the answer correct, show the actual answer to the player.
    if user_guess == random_number:
        return(f"You got the correct number {user_guess}")
    elif user_guess > random_number:
        return("Too High \nGuess again" )
    elif user_guess < random_number:
        return("Too Low \nGuess again")

# Track the number of turns remaining.

attempts = difficulty()
game_is_over = False

while not game_is_over:
    for i in range(attempts, -1, -1):
        if i != 0:
            print(f"You have {i} attempts remaning to guess the number")
            print(compare(guess(), random_number))
        else:
            game_is_over = True 
            print("You've run out of guesses, you lose!")
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

