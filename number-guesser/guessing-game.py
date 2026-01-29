import random
from art import logo

EASY_TURNS = 10
HARD_TURNS = 5

def low_or_high(user_num, num_guess):
    if user_num < num_guess:
        print("Too low.")
        return False
    elif user_num > num_guess:
        print("Too high.")
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
    for i in range(EASY_TURNS):
        print(f"You have {EASY_TURNS - i} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if low_or_high(user_num=user_guess, num_guess=rand_num):
            return
        elif i == 9:
            print("You've run out of guesses, you lose.")
            return
        print("Guess again.")

def hard_guess(rand_num):
    for i in range(HARD_TURNS):
        print(f"You have {HARD_TURNS - i} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if low_or_high(user_num=user_guess, num_guess=rand_num):
            return
        elif i == 4:
            print("You've run out of guesses, you lose.")
            return
        print("Guess again.")
    print()

def number_guesser():
    print(logo)
    rand_num = random.randrange(1, 101)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == 'easy':
        easy_guess(rand_num)
    elif difficulty == 'hard':
        hard_guess(rand_num)

number_guesser()
