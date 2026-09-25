# Lab 1
# Group 2
# Author: Adhamaryz Vargas
# Date: 09/22/2026

# Import the games
from guessing_game import guessing_game
from rps_game import rps_game

if __name__ == "__main__":

    # Welcome message to the program
    print("Welcome! In this program you will be able to play two games: 1. Guessing Game, and 2. Rock-paper-scissors.")
    print("Once you exit a game, you can go back to the same game, choose a different game, or leave the program. It's up to you!")
    print("You are able to start now! \n")

    # Select the game based on user's input
    choice = int(input("Which game do you want to play? 1. Guessing Game, 2. Rock-paper-scissors. "))
    if choice == 1:
        guessing_game()
    elif choice == 2:
        rps_game()

    # Assign value to play
    play = input("Do you want to play again or choose a different game? (Y/N) ")

    # while loop: runs as long as the user inputs "Y" or "YES"
    while play.upper() == "Y" or play.upper() == "YES":
        choice = int(input("Which game do you want to play? 1. Guessing Game, 2. Rock-paper-scissors. "))
        if choice == 1:
            guessing_game()
        elif choice == 2:
            rps_game()
        play = input("Do you want to play again or choose a different game? (Y/N) ")

    # Message if answer is anything but "y" or "yes"
    print("Thank you for playing!")