# Lab 1
# Group 2
# Author: Adhamaryz Vargas
# Date: 09/22/2026

# Import the games
from guessing_game import guessing_game
from rps_game import rps_game

# Select the game based on user's input
choice = int(input("Which game do you want to play? 1. Guessing Game, 2. Rock-paper-scissors. "))
if choice == 1:
    guessing_game()
elif choice == 2:
    rps_game()

# Assign value to play
play = input("Do you want to play again? (Y/N) ")

# while loop: runs as long as the user inputs "Y" or "YES"
while play.upper() == "Y" or play.upper() == "YES":
    choice = int(input("Which game do you want to play? 1. Guessing Game, 2. Rock-paper-scissors. "))
    if choice == 1:
        guessing_game()
    elif choice == 2:
        rps_game()
    play = input("Do you want to play again? (Y/N) ")

# Message if answer is anything but "y" or "yes"
print("Thank you for playing!")