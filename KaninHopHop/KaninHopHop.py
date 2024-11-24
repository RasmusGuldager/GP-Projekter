#This file is for simulating a single game of KaninHopHop

import numpy as np

#Possible outcomes of the kaninhophop dice
dice = ["green", "blue", "purple", "yellow", "red", "rabbit"]

#Roll the dice
def rollDice():
    return dice[np.random.randint(0, 6)]
    
#Function to run the game
def runGame(numberOfPlayers, ruleSet):
    totalRabbitsLeft = 20
    currplayer = 0

    #Set up players with an inital value of 0 rabbits
    players = {}
    for i in range(numberOfPlayers):
        players[f"player{i+1}"] = 0

    #Initialize rabbitHoles with values
    rabbitHoles = {"green": False, "blue": False, "purple": False, "yellow": False, "red": False, }

    #Main while loop for playing the game
    while totalRabbitsLeft > 0:
    
        currRoll = rollDice()

        #If player roll any color
        if currRoll != "rabbit":
            if rabbitHoles[currRoll]:
                rabbitHoles[currRoll] = False
                players[f"player{currplayer+1}"] += 1
            else:
                rabbitHoles[currRoll] = True
                totalRabbitsLeft -= 1

            currplayer = (currplayer + 1) % numberOfPlayers
        #If player roll rabbit
        else:
            if ruleSet == 1:
                players[f"player{currplayer+1}"] -= 1
                totalRabbitsLeft += 1
                currplayer = (currplayer + 1) % numberOfPlayers
            elif ruleSet == 3:
                players[f"player{currplayer+1}"] += 1
                totalRabbitsLeft -= 1
                currplayer = (currplayer + 1) % numberOfPlayers
    #Return dictionary with all players and their points
    return players

