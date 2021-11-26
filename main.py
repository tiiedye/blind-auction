# Blind Auction
from art import logo
import os


# Function to clear console
def clear():
    wipe = '\n' * 100
    print(wipe)


bids = {}
loop = True

while loop:
    print(logo)
    name = input("What is the bidder's name?: ")
    bid_amount = input("How much would you like to bid?: $")

    bids[name] = bid_amount

    add_bidder = input("Is there another bidder? Y/N: ").lower()

    if add_bidder == 'y':
        clear()
    elif add_bidder == 'n':
        loop = False
        clear()
    else:
        clear()
        loop = False
        print("Invalid command, bidding will end")

highest_bidder = ""
highest_bid = 0
for bidder in bids:
    bid = bids[bidder]
    bid = float(bid)
    if bid > highest_bid:
        highest_bidder = bidder
        highest_bid = bid

print(logo)
print(f"The winner of the auction is {highest_bidder}, with ${bids[highest_bidder]}")
