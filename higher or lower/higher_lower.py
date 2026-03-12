import random
from game_data import data
from art import logo, vs

def rand_choice():
    """Selects a random entry from the dictionary, then returns entry to variable."""
    rand_select = random.choice(data)
    return rand_select

# Compare follower counts, then return selection with highest follower count.
def compare_followers(acct1, acct2):
    """Compares follower counts for both accounts, then return account with highest followers."""
    if acct1["follower_count"] > acct2["follower_count"]:
        return 'A'
    elif acct1["follower_count"] < acct2["follower_count"]:
        return 'B'

# Set score to 0, then print game logo.
score = 0
print(logo)
lose_condition = False

while lose_condition == False:
    # Both Instagram accounts randomly selected at start of game.
    if score == 0:
        insta_acct1 = rand_choice()
    else:
        print(f"You're right! Current score: {score}")
    insta_acct2 = rand_choice()

    print(f"Compare A: {insta_acct1["name"]}, a {insta_acct1["description"]}, from {insta_acct1["country"]}.")
    print(vs)
    print(f"Compare B: {insta_acct2["name"]}, a {insta_acct2["description"]}, from {insta_acct2["country"]}.")

    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    # Returns 'A' if first account has more followers, 'B' if second account has more followers.
    compare_result = compare_followers(acct1=insta_acct1, acct2=insta_acct2)

    # Set first Instagram choice to player correct guess, increment player score by 1. Otherwise, game over.
    if user_choice == compare_result:
        if user_choice == 'B':
            insta_acct1 = insta_acct2
        score += 1
        print('\n' * 20)
    else:
        lose_condition = True
print(f"Game over. Your final score was: {score}")
