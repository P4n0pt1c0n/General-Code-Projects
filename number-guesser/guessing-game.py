import random
from art import logo

EASY_TURNS = 11
HARD_TURNS = 6

def low_or_high(user_num, num_guess):
    if user_num < num_guess:
        print("Too low.\nGuess again.")
        return False
    elif user_num > num_guess:
        print("Too high.\nGuess again.")
        return False
    elif user_num - num_guess == 0:
        print(f"You got it! The answer was {num_guess}")
        return True

def set_difficulty(difficulty):
    if difficulty == 'easy':
        return EASY_TURNS
    elif difficulty == 'hard':
        return HARD_TURNS

def easy_guess(rand_num):
    for i in range(1, 11):
        print(f"You have {11 - i} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if low_or_high(user_num=user_guess, num_guess=rand_num):
            return

def hard_guess(rand_num):
    for i in range(1, 6):
        print(f"You have {6 - i} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if low_or_high(user_num=user_guess, num_guess=rand_num):
            return

def number_guesser():
    print(logo)
    rand_num = random.randrange(1, 101)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    turn_num = set_difficulty(difficulty)
    for i in range(1, turn_num):
        print(f"You have {turn_num - i} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
    if difficulty == 'easy':
        easy_guess(rand_num)
    elif difficulty == 'hard':
        hard_guess(rand_num)

number_guesser()
