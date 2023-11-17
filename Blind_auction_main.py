from replit import clear

from art import logo
print(logo)

bids={}
bid_finished=False
def highest_bid(biddiing_record):
  highest_bid=0
  winner=""
  for bidder in biddiing_record:
    amount=biddiing_record[bidder]
    if amount>highest_bid:
      highest_bid=amount
      winner = bidder
  print(f"Winner is {winner} with a bid of ${highest_bid}") 
  
while not bid_finished:
  name=input("Enter the name of the bidder: ")
  price=int(input("Enter yout bid: $"))
  bids[name]=price
  
  another_bid = input("Type 'yes' if you want to go again or Otherwise type 'no'.\n")
  if another_bid=="no":
    bid_finished=True
    highest_bid(bids)
  elif another_bid=="yes":
    clear()
    
  
