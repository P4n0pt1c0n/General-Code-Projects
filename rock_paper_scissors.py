import random

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

game_choices = [rock, paper, scissors]
computer_input = random.randint(0, 2)
player_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors."))
print(f"Player chose:\n {game_choices[player_input]}\n")
print(f"Computer chose:\n {game_choices[computer_input]}\n")
# Checks rock against scissors.
if player_input == 0 and computer_input == 2:
    print("You win!")
# Checks scissors against rock.
elif computer_input == 0 and player_input == 2:
    print("You lose.")
elif computer_input > player_input:
    print("You lose.")
elif player_input > computer_input:
    print("You win!")
elif player_input == computer_input:
    print("It's a draw.")

