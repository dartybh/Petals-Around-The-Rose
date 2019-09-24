# Play Petals Around the Rose
# Author: Luke Dart
# Updated: 24/9/2019

#Import libraries
import random

#Initiate stats
streak = 0
maxstreak = 0
attempts = 0
correct = 0



#Define dice
dice = []

#Define function to roll five dice
def roll():
	dice.clear()
	for x in range(5):
		dice.append(random.randint(1, 6))

#Recursive function to play Petals Around The Rose
def play():
	global streak, maxstreak, attempts, correct
	
	#Call function to roll the dice
	roll()

	#Score the roll
	score = 0
	for x in dice:
		if x == 3:
			score += 2
		elif x == 5:
			score += 4

	#Tell the user what the dice roll result are
	print("\nThe dice rolled are", str(dice)[1:-1])

	#Ask the user to guess the score
	guess = input("What is the score? ")
	while guess.isdigit() == False:
		guess = input("Please enter a number for your guess: ")
		
	#Respond based on user's guess and update play stats
	attempts += 1

	if int(guess) == score:
		print ("\nCorrect! The score is", str(guess))
		correct += 1
		streak += 1
		if streak > maxstreak:
			maxstreak = streak
	else:
		print("\nNo, the score is", score)
		streak = 0

	#Ask user to play another round or quit
	cont = input("\nPlay another round? y/n ")
	if cont == "y"or cont == "Y":
		play()
	else:
		print("\nYour play stats are:\nTotal attempts:", attempts, "\nCorrect guesses:", correct, "\nLongest streak:", maxstreak, "\n\nPress enter to exit.")
		input()

#Introduce the game
print("\n---<----(@ \n\nPetals around the rose\n\n")

print("            *     * *   * *   * *")
print(" *    * *    *           *    * *")
print("              *   * *   * *   * *")

print("\n\nThe name of the game is important.")
print("Each time the dice are rolled you will try and guess the score.")
print("The score can only be zero or an even number.")
print("You will then be told if you were correct or not.\n")

play()



