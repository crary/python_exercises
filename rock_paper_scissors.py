import random
import time

playList = [ "rock", "paper", "scissors" ]

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
    elif player1 == "scissors" and player2 == "rock":
        return "player2"
    elif player1 == "paper" and player2 == "scissors":
        return "player2"
    elif player1 == player2:
        return "tie"     

# Run game until winner declaired
def rpsWinner():
    pickRPS()
    print("Player 1: "+ player1)
    print("Player 2: "+ player2)
    outCome = battleHand(player1,player2)
    print(outCome)
    if outCome == "tie":
        # Break the tie
        while True:
            time.sleep(1)
            print(pickRPS())
            outCome = battleHand(player1,player2)
            print(outCome)
            if outCome != "tie":
                break

rpsWinner()
