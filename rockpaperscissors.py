# Random is a library with functions that randomly selects something
# Typing module adds support for type hints
import random
from typing import List

# I created a list of strings which is the different available options for the user to choose
choices: List[str] = ["rock", "paper", "scissors"]
print(type(choices))
computer: str = random.choice(choices)
print(type(computer))
player: str = None
player: Union[str, None]

# The .lower() method is used to ensure that the string is converted to lower case
# The input() function is used to take the user's input and returns it
while player not in choices:
    player: str = input("Choose between rock, paper or scissors?: ").lower()

#  If, elif, else  statements are used to compare with the input value with the value that the user selects
if player == computer:
    print("Computer: ", computer)
    print("Player: ", player)
    print("Tie!")

# I put together the different possibilities of combination for rock, paper and scissors
# It will print you lose or you win depending on the move that is made by the computer
elif player == "rock":
    if computer == "paper":
        print("Computer: ", computer)
        print("Player: ", player)
        print("You lose!")
    if computer == "scissors":
        print("Computer: ", computer)
        print("Player: ", player)
        print("You win!")
    elif player == "scissors":
        if computer == "rock":
            print("Computer ", computer)
            print("Player: ", player)
            print("You lose!")
        if computer == "paper":
            print("Computer ", computer)
            print("Player ", player)
            print("You win!")
    elif player == "paper":
        if computer == "rock":
            print("Computer ", computer)
            print("Player ", player)
            print("You win!")
        if computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lose!")
