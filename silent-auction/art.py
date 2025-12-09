from art import logo
# TODO-1: Ask the user for input
def find_highest_bidder (bidding_dictionary):
    max_bid = 0
    max_name = ""
    for name in bidding_dictionary:
        if bidding_dictionary[name] > max_bid:
            max_name = name
            max_bid = bid_dict[name]
    print(f"The winner of the auction is {max_name} with a bid of ${max_bid}")

bid_dict = {}
continue_bid = True

print(logo)
print("Welcome to the secret auction program.")

while continue_bid:
    username = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bid_dict.update({username: bid})
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if other_bidders == 'no':
        continue_bid = False
        find_highest_bidder(bid_dict)
    elif other_bidders == 'yes':
        print("\n" * 20)
