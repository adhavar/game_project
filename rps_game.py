#Lab 1
# Group 2
# Author =Christian S
# 09/25/2026

import random

def rps_game():
  play = "yes"
  
  while play == "yes":
    computer = random.randint(1, 3)
    
    user = int(input("Enter your choice: 1. paper, 2. scissors, 3. rock: "))
    
    if user == computer:
      print("It is a tie!")
    
    elif user == 1 and computer == 3:
      print("You win!")
    
    elif user == 2 and computer == 1:
      print("You win!")
    
    elif user == 3 and computer == 2:
      print("You win!")
    
    else:
      print("Computer wins!")
    
    play = input("Do you want to play again? (yes/no): ")

  if __name__== "__main__":
     rps_game()