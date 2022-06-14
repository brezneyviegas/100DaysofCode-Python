#import all other files

from art import logo, vs
#import random 
import random
#import the game data 
from game_data import data
import os

#Feature to check if the user wants to play the game or not
print(logo)
score = 0
object_b = random.choice(data)

# #check if the user want to play the game
# wants_to_play = False
# user_input = input("Do yo want to play higher or lower? type 'Y' for yes and 'n' for no: ")
# if user_input == "n":
#       wants_to_play = False
# elif user_input == "y":
#       wants_to_play = True
# else:
#       print("Please enter a valid input")

#function to format the data 
def format_data(object):
      object_name = object["name"]
      object_desc = object["description"]
      object_country = object["country"]

      return(f"{object_name}, a {object_desc}, from {object_country}")

#function to check the guess is correct 
def check_guess(user_input, a_follower, b_follower):
      if a_follower > b_follower:
            return user_input == "a"
      else:
            return user_input =="b"

#loop the game until the user guess is wrong     
end_of_game = False
while not end_of_game:

      #function to pick random game data 
      object_a = object_b
      object_b = random.choice(data)
      if object_a == object_b:
            object_b = random.choice(data)


      print(f"Compare A: {format_data(object_a)}")
      print(vs)
      print(f"Against B: {format_data(object_b)}")

      #Function to take user input
      user_input = input("Who has more followers? Type 'A' or 'B': ").lower()

      a_follower = object_a["follower_count"]
      b_follower = object_b["follower_count"]

      is_correct = check_guess(user_input, a_follower, b_follower)

      #clear the screen for the next run 
      os.system('cls' if os.name == 'nt' else 'clear')

      #function to display the score
      if is_correct:
            score += 1
            print(f"you got it right!  Current score : {score}.")
      else:
            print(f"sorry thats wrong. Your Final score was: {score}.")
            end_of_game = True

      

      

     

   

