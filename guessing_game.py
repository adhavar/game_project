# Lab 1
# Group 2
# Author: Kezlyn margareth
# Date: 9/22/2026

import random

def guessing_game():
    """
    Runs a number guessing game where the player tries to guess
    a randomly generated number between 1 and 100. The player
    receives up to 5 attempts and gets hints if the guess is
    too high or too low.

    Author: Kezlyn Margareth
    """
    print("Hi There! Welcome to Guessing Game!")
    print("I'm thingking of a number between 1 to 100.")
    print("I will give you 5 attemps. Try to guess what the number is.")
    print("Good luck!")

    number = random.randint(1,100)
    i = 5

    while i > 0:
        user_number = int(input('\nEnter your guess: '))
        if user_number < number:
            print("Too low.", end= " ")
        elif user_number > number:
            print("Too high.", end= " ")
        else:
            print("You guessed it! Congratulation!")
            break

        i -= 1

        if i == 1:
            print("Try again!\nYou only have 1 more attempt")
        elif i > 0:
            print("Try again!\nYou have", i, "more attempts")
        

    if i == 0:
        print(f'You lost! The number is {number}')

if __name__== "__main__":
    guessing_game()
    
    
