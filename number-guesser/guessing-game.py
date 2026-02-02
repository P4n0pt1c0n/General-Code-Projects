import random
from art import logo

EASY_TURNS = 10
HARD_TURNS = 5

def low_or_high(user_num, num_guess):
    # Returns False if guessed num. is incorrect to resume loop.
    if user_num < num_guess:
        print("Too low.")
        return False
    elif user_num > num_guess:
        print("Too high.")
        return False
    elif user_num - num_guess == 0:
        print(f"You got it! The answer was {num_guess}")
        return True

def set_difficulty(turn_choice):
    # Return num. of turns to 10 if easy, 5 if hard.
    if turn_choice == 'easy':
        return EASY_TURNS
    elif turn_choice == 'hard':
        return HARD_TURNS

def guess_loop(turn_count, num_to_guess):
    i = 0
    while i <= turn_count - 1:
        print(f"You have {turn_count - i} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        # If user guesses correct num., return True and end loop early.
        if low_or_high(user_num=user_guess, num_guess=num_to_guess):
            return
        # If user runs out of guesses, print lose message then exit function early.
        elif i + 1 == turn_count:
            print("You've run out of guesses, you lose.")
            return
        print("Guess again.")
        i += 1

def number_guesser():
    print(logo)
    rand_num = random.randrange(1, 101) # Generate rand. num. to guess.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    # Sets number of turns based on difficulty chosen, which will be passed to guessing function.
    turns = set_difficulty(turn_choice=difficulty)
    # Starts guess loop function. Pass num. of turns and num. to guess into function.
    guess_loop(turn_count=turns, num_to_guess=rand_num)

number_guesser()
