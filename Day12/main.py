#Number Guessing Game Objectives:

# Include an ASCII art logo.
from art import logo, win

#Create a Random number will be used for comparering with user input
import random


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to get user to pick difficulty 
def difficulty():
    user_input = input("Choose a dificulty: Type 'easy' or 'hard': ")
    if user_input == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
def compare(user_guess, random_number, turns):
    # If they got the answer correct, show the actual answer to the player.
    
    if user_guess > random_number:
        print("Too High" )
        return turns - 1
    elif user_guess < random_number:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got the correct number {user_guess}")
        print(win)

# Track the number of turns remaining.


def game():
      print(logo)
  #Choosing a random number between 1 and 100.
      print("Welcome to the Number Guessing Game!")
      print("I'm thinking of a number between 1 and 100.")
      print(f"Pssst, the correct answer is {random_number}") 

      turns = difficulty()
      #Repeat the guessing functionality if they get it wrong.
      user_guess = 0
      while user_guess != random_number:
        print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
        user_guess = int(input("Make a guess: "))
        if user_guess < 1 or user_guess > 100:
            print("Please enter a number between 1 and 100")

    #Track the number of turns and reduce by 1 if they get it wrong.
        turns = compare(user_guess, random_number, turns)
        if turns == 0:
          print("You've run out of guesses, you lose.")
          return
        elif user_guess != random_number:
          print("Guess again.")


game_is_over = False
while not game_is_over:
    random_number = random.randint(1,100)
    game()
    play_again = input("Would you like to play again? Yes or No: ").lower
    if play_again != "yes":
        game_is_over = True