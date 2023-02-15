
import random
import time
from tkinter.tix import Tree

playList = [ "rock", "paper", "scissors" ]
#player1 = ""
#player2 = ""

## Randomly select Rock, Paper or Scissor for both players
def pickRPS ():
    global player1
    global player2
    player1 = random.choice(playList)
    player2 = random.choice(playList)
    return  player1, player2

## Decide winner between players
def battleHand(player1,player2):
    if player1 == "rock" and player2 == "paper":
        return "player2"
    elif player1 == "paper" and player2 == "rock":
        return "player1"
    elif player1 == "scissors" and player2 == "paper":
        return "player1"
    elif player1 == "rock" and player2 == "scissors":
        return "player1"
    elif player1 == player2:
        return "tie"
        # print("Its a tie")
        # time.sleep(1)
        # print("Breaking tie...")
        # print(pickRPS())
        # while True:
        #     print(pickRPS())
        #     print(player1)
        #     print(player2)
        #     time.sleep(1)
        #     if player1 == "rock" and player2 == "paper":
        #         return "player2"
        #     elif player1 == "paper" and player2 == "rock":
        #         return "player1"
            
        

def rpsWinner():
    pickRPS()
    print("Player 1: "+ player1)
    print("Player 2: "+ player2)
    print(battleHand(player1,player2))
    # if battleHand(player1,player2) == "tie":
    #     while True:
    #         pickRPS()
    #         print(battleHand(player1,player2))






rpsWinner()
print("\n")
rpsWinner()