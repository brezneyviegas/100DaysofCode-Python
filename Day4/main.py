rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random 

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
comp_input = random.randint(0,2)

list = [rock, paper, scissors]


print(f"{list[user_input]}")
print(f"Computer Chose:\n{list[comp_input]}")
if user_input == comp_input:
  print(f"Draw try again!")
elif user_input == 0 and comp_input == 2:
  print (f"User Won")
elif user_input == 1 and comp_input == 0:
  print (f"User Won")
elif user_input == 2 and comp_input == 1:
  print (f"User Won")
else:
  print (f"You Lose")
