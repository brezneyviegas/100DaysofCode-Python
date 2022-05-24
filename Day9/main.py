from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
bid_dict ={}

#function to get users to enter a name and bid amount
def ubid():
  user_name = input("What is your name?: ")
  user_bid = int(input("What is your bid?: £"))
  bid_dict[user_name] = user_bid

#function to get the winning bid and user from dict
def find_winner(all_bids):
  highest_bid = 0
  winner = ""
  for bidder in all_bids:
    bid_amount = all_bids[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} the winning bid was £{highest_bid}")


#Loop to check there are no more users
end_game = False
while not end_game:
  ubid()
  another_user = input("Is there another user? yes or no: ")
  if another_user == "yes":
    clear()
    end_game = False
  else:
    end_game
    find_winner(bid_dict)
      
    
