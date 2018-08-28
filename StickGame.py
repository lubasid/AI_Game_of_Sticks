# Author: Lyubov Sidlinskaya
# Course: CSC 
# Assignment: HW1 Stick Game
#-------------------------------------

#Imports
import random


maxNum = 10
gameBins = [[1,2,3] for i in range(0, maxNum + 1)]


def initGame():
	
	random.seed()
	stickNumber = random.randint(1, maxNum)
	aiWins = False
	
	print ("\nSTARTING GAME: ")
	print ("sticks in game:    ", stickNumber)
	print ("-------------------------------------\n")

	humanCounter =[]
	aiCounter = []

	while stickNumber > 0:
		
		humanPick = humanPlayer()
		print ("THE HUMAN PICKED:     ", humanPick)
		print ([stickNumber, humanPick])
		humanCounter.append([stickNumber, humanPick])
		stickNumber = stickNumber - humanPick
		print ("Sticks left:        ", stickNumber )

		print ("")

		if stickNumber > 0:

			aiPick = aiPlayer(stickNumber)
			print ("THE AI PICKED:     ", aiPick)

			print ([stickNumber, aiPick])
			aiCounter.append([stickNumber, aiPick])
			stickNumber = stickNumber - aiPick
			print ("Sticks left:        ", stickNumber )
			print ("")
			if stickNumber < 1:
				print ("AI LOSES")
		
		else:
			aiWins = True
			print ("HUMAN LOSES")

	if aiWins:
		print ("AI winssssssss\n")
	
		for i in range(len(aiCounter)):
			currentItem = aiCounter[i]
			updateBin = currentItem[0]
			updateCount = currentItem[1]
			gameBins[updateBin].append(updateCount)

			print ("add     ", updateCount, " to    ", updateBin)
		# print (gameBins[4].append)

	print (humanCounter)
	print (aiCounter)

	print ("\n-----------------------\n")
	print (gameBins)


def aiPlayer(stick):
	if stick >= 3:
		currentBin = gameBins[stick]
		print (currentBin)
		getRandom  = random.choice(currentBin)
		print (getRandom)
		return getRandom
	elif stick ==2:
		getRandom  = random.randint(1, 2)
		return getRandom

	elif stick ==1:

		print ("Artie loses")
		return 1
		
	


def humanPlayer():
	maxNum = 3
	random.seed()
	sticksTaken = random.randint(1, maxNum)
	# print ("selected     ", sticksTaken)
	return sticksTaken


def main():
	initGame()


	#print ("hello world")#

main()