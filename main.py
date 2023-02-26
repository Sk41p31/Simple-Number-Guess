#Number Guessing Game

import random
from replit import clear
import art

HARD_LEVEL = 5
EASY_LEVEL = 10

def guess(number, answer) :
    if number == answer :
        print(f"\nYour guess was correct! {answer} was the number!\n")
        print(art.you_won)
        return True
    elif number < answer :
        print("Too low!")
        return False
    else :
        print("Too high!")
        return False

def number_guess() :

    
    incorrect_choice = True
    x = random.randint(1,100)
    # Debug
    # print(f"Number is {x}\n")
    
    
    clear()
    print(art.logo)
    print("\nWelcome to Number Guess! Guess a number between 1 and 100!")
    
    while incorrect_choice :
        difficulty = input("Choose between 'hard' and 'easy' difficulty: ")
        if difficulty == 'hard' :
            remaining_tries = HARD_LEVEL
            incorrect_choice = False
        elif difficulty == 'easy' :
            remaining_tries = EASY_LEVEL   
            incorrect_choice = False
        else :
            print("Wrong choice, try again!")
    
    
    
    game_over = False
    while not game_over :
        print("\n=================================\n")
        print(f"You have {remaining_tries} remaining tries.")
        guessed_number = int(input("Take a guess: "))
    
        game_over = guess(guessed_number, x)
        remaining_tries -= 1
        if not remaining_tries :
            game_over = True
            print(f"\nYou ran out of tries! {x} was the number!\n")
            print(art.you_lost)
    
    try_again = input("To try again, type 'y': ")
    if try_again == 'y' :
        number_guess()


number_guess()