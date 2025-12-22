import random
from art import logo

def score_calculator(current_hand):
    if sum(current_hand) == 21:
        return 0

    if 11 in current_hand and sum(current_hand) > 21:
        current_hand.remove(11)
        current_hand.append(1)

    return sum(current_hand)

def card_dealer():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def win_decision(comp_score, user_score):
    if comp_score == user_score:
        return "Draw."
    elif user_score > 21:
        return f"You lose. Your score was: {user_score}"
    elif comp_score > 21:
        return f"Opponent loses with a score of: {comp_score}. Your score was: {user_score}. You win!"
    elif user_score == 0:
        return "Player has jackpot, player wins!"
    elif comp_score == 0:
        return "Lose, opponent has Blackjack."
    elif user_score > comp_score:
        return f"Your score was {user_score}, the opponent's score was {comp_score} You win!"
    else:
        return f"Your score was {user_score}, the opponent's score was {comp_score} You lose."


def play_game():
    resume_game = True
    player_cards = []
    npc_cards = []
    player_score = -1
    npc_score = -1

    print(logo)

    for i in range(0, 2):
        player_cards.append(card_dealer())
        npc_cards.append(card_dealer())

    player_score = score_calculator(current_hand=player_cards)
    npc_score = score_calculator(current_hand=npc_cards)

    while resume_game:
        print(f"Your cards:  {player_cards}\nYour current score: {player_score}")
        print(f"Computer's first card: {npc_cards[0]}")
        if player_score == 0 or npc_score == 0 or player_score > 21:
            resume_game = False
        else:
            player_input = input("Type 'y' to get another card, type 'n' to pass: ")
            if player_score <= 21 and player_input == 'y':
                player_cards.append(card_dealer())
                player_score = score_calculator(current_hand=player_cards)
            elif player_input == 'n' or player_score > 21:
                resume_game = False

    while npc_score < 17:
        npc_cards.append(card_dealer())
        npc_score = score_calculator(current_hand=npc_cards)

    print(f"Player's final hand is: {player_cards}")
    print(f"Opponent's final hand is: {npc_cards}")
    print(win_decision(comp_score=npc_score, user_score=player_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': "):
    print("\n" * 20)
    play_game()
