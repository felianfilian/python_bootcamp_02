

def start():
    more_input = "y"
    while more_input == "y":
        name = input("Your name:\n")
        bid = input("Your bid:\n")
        more_input = input("More bidder? (y/n):\n")

    highest_bid = 0
    print("The highest bid: " + name + " with " + bid + " $")