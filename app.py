#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")


""" game multiplayer, where the computer will be your opponent and can randomly choose one of the elements (rock, paper, or scissors) for each move, just like you. Your interaction in the game will be through the console (Terminal).
 The game will be played in a total of 3 rounds. The player who wins the most rounds wins the game. If both players choose the same element, it will be a tie and no one will win that round.
 code in python

The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
By the end of each round, the player can choose whether to play again.
Display the player's score at the end of the game.
The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.
In your GitHub Codespaces, use the provided specifications to create prompts that can be utilized by GitHub Copilot to assist you in developing the minigame. Remember, GitHub Copilot uses comments to understand context and provide accurate suggestions during development.
"""

import random
import time

def play():
    print("Welcome to Rock, Paper, Scissors!")
    time.sleep(1)
    print("You will be playing against the computer.")
    time.sleep(1)
    print("The first to win 3 rounds wins the game.")
    time.sleep(1)
    print("Good luck!")
    time.sleep(1)
    print("Rock...")
    time.sleep(1)
    print("Paper...")
    time.sleep(1)
    print("Scissors...")
    time.sleep(1)
    print("Shoot!")

    player_score = 0
    computer_score = 0

    while player_score < 3 and computer_score < 3:
        player = input("What do you choose? ").lower()
        if player == "quit" or player == "q":
            break
        random_num = random.randint(0,2)
        if random_num == 0:
            computer = "rock"
        elif random_num == 1:
            computer = "paper"
        else:
            computer = "scissors"
        print(f"The computer plays {computer}.")

        if player == computer:
            print("It's a tie!")
        elif player == "rock":
            if computer == "scissors":
                print("You win!")
                player_score += 1
            else:
                print("The computer wins!")
                computer_score += 1
        elif player == "paper":
            if computer == "rock":
                print("You win!")
                player_score += 1
            else:
                print("The computer wins!")
                computer_score += 1
        elif player == "scissors":
            if computer == "paper":
                print("You win!")
                player_score += 1
            else:
                print("The computer wins!")
                computer_score += 1
        else:
            print("Please enter a valid move!")

        print(f"Your score: {player_score}")
        print(f"Computer score: {computer_score}")
        print("")

    if player_score > computer_score:
        print("CONGRATS, YOU WON!")
    elif player_score == computer_score:
        print("IT'S A TIE")
    else:
        print("OH NO :( THE COMPUTER WON...")
    print("Thanks for playing!")

play()



