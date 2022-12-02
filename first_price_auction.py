

def start():
    more_input = "y"
    bids = {}
    highest_bid = 0
    winner = ""
    while more_input == "y":
        name = input("Your name:\n")
        bid = int(input("Your bid:\n"))
        bids[name] = bid
        more_input = input("More bidder? (y/n):\n")
    for person in bids:
        bid_amount = bids[person]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = person
    print(f"the winner is {winner} with a bid of {highest_bid}")
