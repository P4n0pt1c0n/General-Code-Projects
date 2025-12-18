import random
from art import logo

def score_calculator(current_hand):
    score = 0
    for card in current_hand:
        score += card

    return score

resume_game = True
player_cards = []
npc_cards = []
player_score = 0
npc_score = 0
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play_game = input("Do you want to play a game of Balckjack? Type 'y' or 'n'").lower()

if play_game == 'y':
    print(logo)
    continue_draw = True
    while resume_game:
        if len(player_cards) >= 2:
            print(f"Your cards: {player_cards}")
            if get_more_cards == 'y' or continue_draw == True:
                player_cards.append(cards[random.randrange(0, 13)])
            elif not npc_score > 16:
                npc_cards.append(cards[random.randrange(0, 13)])
            print(npc_cards)
        else:
            player_cards.append(cards[random.randrange(0, 13)])

        player_score = score_calculator(current_hand=player_cards)
        npc_score = score_calculator(current_hand=npc_cards)

        if player_score > 21:
            resume_game = False
            print(f"You lose. Your score was: {player_score}")
        elif npc_score > 21:
            resume_game = False
            print(f"NPC loses with a score of: {npc_score}. Your score was: {player_score}. You win!")
        elif player_score == 21:
            resume_game = False
            print("Player has jackpot, player wins!")
        elif npc_score == 21:
            resume_game = False
            print("Lose, opponent has Blackjack.")

        get_more_cards = input("Type 'y' to get another card, type 'n' to pass: ")

elif play_game =='n':
    print("Ending game.")
