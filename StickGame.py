# Author: Lyubov Sidlinskaya
# Course: CSC 540 
# Assignment: HW1  - Game of Sticks
#
# Description:  A game of Sticks where the game is randomly started
# by the ai or human player. Each player can only take 1-3 sticks.
# The AI draws plays from appropriate bins containing values 1-3.
# While the human selects the values randomly. If the AI wins,
# the bins are updated to reflect the winning value selected at
# certain bins. After the training has completed, the highest value 
# from each bin is printed as output.

# TO RUN PROGRAM:    python StickGame.py
#-> enter numbers of times to train AI -> enter
#
# python version 3.6.5
#-------------------------------------

#Imports
import random
import sys

# The max number of bins.
maxNum = 100
# The table for holding the initial contents ([1,2,3]) of each bin. 
gameBins = [[1,2,3] for i in range(0, maxNum + 1)]

# Function which removes the illegal moves from the game bins. 
def setBins():
	gameBins[1].remove(2)
	gameBins[1].remove(3)
	gameBins[2].remove(3)
	gameBins[2].remove(2)
	gameBins[3].remove(3)
	
# Function which initilizes the game. 
# It randomly selects the AI or Human to begin the game. 
def initGame(humanWinCount, aiWinCount):

	# Randomly seed the function.
	random.seed()
	# Begin game with a random amount of sticks from [10, 100]
	stickNumber = random.randint(10, maxNum)

	# Random value to determine who starts the game. 
	selectRandPlayer = random.randint(1,2)
	
	# Begins game randomly.
	# 1 == Human begins game. 2 == AI begins game.
	if selectRandPlayer == 1:
		startPlayer = "human"
		hWins,aWins = playGame(startPlayer, stickNumber, humanWinCount, aiWinCount)
	else:
		startPlayer = "ai"
		hWins,aWins = playGame(startPlayer, stickNumber, humanWinCount, aiWinCount)
	return hWins, aWins
	
# Function which plays game until sticks left are zero. 
def playGame(startPlayer, stickNumber, humanWinCount, aiWinCount):
	
	# List to keep track of values each player selected.
	humanTrack =[]
	aiTrack = []

	while stickNumber > 0:
		# If one stick left. Current game round will terminate. 
		if stickNumber == 1:
			# Updates the score with the scoreKeeper () function. 
			hWins,aWins = scoreKeeper(startPlayer, aiTrack, humanWinCount, aiWinCount)
			stickNumber = stickNumber - 1

		# Human starting game.
		elif startPlayer == "human":
			# Returns random value (1-3) from humanPlayer function().
			humanPick = humanPlayer(stickNumber)
			# Add the choice to tracking list. 
			humanTrack.append([stickNumber, humanPick])
			stickNumber = stickNumber - humanPick
			# Next turn is the ai.
			startPlayer = "ai"

		# AI starting game. 
		elif startPlayer == "ai":
			aiPick = aiPlayer(stickNumber)
			aiTrack.append([stickNumber, aiPick])
			stickNumber = stickNumber - aiPick
			# Next turn is the human.
			startPlayer = "human"

	return hWins, aWins 

# Function which keeps track of the wins for Human & AI. 
def scoreKeeper(losingPlayer, aiTrack, humanWinCount, aiWinCount):
	if losingPlayer == "human":
		aiWinCount +=1
		updateBins(aiTrack)
		return humanWinCount, aiWinCount

	elif losingPlayer == "ai":
		humanWinCount += 1
		return humanWinCount, aiWinCount

# Function which updates game bins when AI wins. 
def updateBins(aiTrack):
	for i in range(len(aiTrack)):
		currentItem = aiTrack[i]
		# The bin that needs to be updated.
		updateBin = currentItem[0]
		# The digit that will be inserted into bin. 
		updateCount = currentItem[1]
		# Updates original bins winning values. 
		gameBins[updateBin].append(updateCount)

# Function which returns a randomly slected value from 
# bin of the stick argument passed. 
def aiPlayer(stick):
	currentBin = gameBins[stick]
	getRandom  = random.choice(currentBin)
	return getRandom

# Function which returns a randomly slected value of 1-3	
def humanPlayer(stick):
	if stick > 3:
		selectRandom = random.randint(1,3)
		return selectRandom
	elif stick == 3:
		selectRandom  = random.randint(1, 2)
		return selectRandom
	elif stick == 2:
		selectRandom  = random.randint(1, 1)
		return selectRandom
	elif stick == 1:
		return 1

# Function which prints the AI bins after training. 
def printChart(trainCount, aiWins):
	count = -1
	print ("GAME BINS INDEX & CONTENTS: \n")
	print ("index\t", "value most selected" )
	for count, item in enumerate(gameBins, start=0):
		num = max(item, key = item.count)
		if count >=10:
			print(count,"\t", num)

	# Print accuracy.
	print ("\nAI win %:     ", (aiWins / trainCount) )

def main():
	# User input for the number of times AI should be trained. 
	try:
		trainCount = int(input("Enter number for AI training:    \n"))
	except ValueError:
		print ("Enter a valid numerical value:  Example:  20000")
		sys.exit()
		
	curCount = 1
	# Counters to determine accuracy.
	aiWinCount = 0
	humanWinCount = 0
	finalHCount, finalACount = 0, 0
	# Removes illegal moves from bins. 
	setBins()
	# Starts at 1, ends when curCount == to input training value. 
	while curCount <= trainCount:
		hWins, aWins = initGame(humanWinCount, aiWinCount)
		finalHCount += hWins
		finalACount += aWins
		curCount +=1

	# print("\nTotal human wins: ", finalHCount, "   Total ai wins: ", finalACount)
	print ()
	printChart(trainCount, finalACount)

main()