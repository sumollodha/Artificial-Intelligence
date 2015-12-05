import readGame
import config

#######################################################
# These are some Helper functions which you have to use 
# and edit.
# Must try to find out usage of them, they can reduce
# your work by great deal.
#
# Functions to change:
# 1. is_corner(self, pos):
# 2. is_validMove(self, oldPos, direction):
# 3. getNextPosition(self, oldPos, direction):
# 4. getNextState(self, oldPos, direction):
#######################################################

class game:
	def __init__(self, filePath):
        	self.gameState = readGame.readGameState(filePath)
                self.nodesExpanded = 0
                self.g=0
		self.trace = []
	
	def is_corner(self, pos):
		########################################
		# You have to make changes from here
		# check for if the new positon is a corner or not
		# return true if the position is a corner
		########################################
		dim = len(self.gameState)
		########################################
	    #1) checking for out of bound positions
	    #2) checking for corner positions
	    ########################################
		if(pos[0] < 0 or pos[1] < 0 or pos[0] >= dim or pos[1] >= dim):
			return True
		elif  (self.gameState[pos[0]][pos[1]] == -1):
			return True
		else:
			return False	

	def getIntermediatePosition(self, oldPos, direction):
		#########################################
		# This is needed as applying direction gives a intermediate position
		#########################################
		newX = oldPos[0] + config.DIRECTION[direction][0]
		newY = oldPos[1] + config.DIRECTION[direction][1]
		newPos = (newX, newY) 
		return newPos 

	
	def getNextPosition(self, oldPos, direction):
		#########################################
		# YOU HAVE TO MAKE CHANGES HERE
		# See DIRECTION dictionary in config.py and add
		# this to oldPos to get new position of the peg if moved
		# in given direction , you can remove next line
		# ########################################
		#It will first generate an intermediate positiona and feed this again to
		# get final position
		###########################################
		interPos = self.getIntermediatePosition(oldPos, direction)
		newPos = self.getIntermediatePosition(interPos, direction)
		#print "", newPos
		return newPos 
	
	
	def is_validMove(self, oldPos, direction):
		#########################################
		# DONT change Things in here
		# In this we have got the next peg position and
		# below lines check for if the new move is a corner
		newPos = self.getNextPosition(oldPos, direction)
		if self.is_corner(newPos):
			return False	
		#########################################
		
		########################################
		# YOU HAVE TO MAKE CHANGES BELOW THIS
		# check for cases like:
		# if new move is already occupied
		# or new move is outside peg Board
		# Remove next line according to your convenience
		dim = len(self.gameState)
		interPos = self.getIntermediatePosition(oldPos, direction)
		if(self.gameState[oldPos[0]][oldPos[1]] == 0 or self.gameState[oldPos[0]][oldPos[1]] == -1):
			return False
		if(self.gameState[interPos[0]][interPos[1]] != 1):
			return False
		elif (self.gameState[newPos[0]][newPos[1]] != 0):
			return False
		else:
			return True
	
	def getNextState(self, oldPos, direction):
		###############################################
		# DONT Change Things in here
		self.nodesExpanded += 1
		if not self.is_validMove(oldPos, direction):
			print "Error, You are not checking for valid move"
			exit(0)
		###############################################
		
		###############################################
		# YOU HAVE TO MAKE CHANGES BELOW THIS
		# Update the gameState after moving peg
		# eg: remove crossed over pegs by replacing it's
		# position in gameState by 0
		# and updating new peg position as 1
		self.gameState[oldPos[0]][oldPos[1]] = 0
		interPos = self.getIntermediatePosition(oldPos, direction)
		self.gameState[interPos[0]][interPos[1]] = 0
		newPos = self.getIntermediatePosition(interPos, direction)
		self.gameState[newPos[0]][newPos[1]] = 1
		readGame.totalNodeExpended += 1
		self.trace.append((oldPos[0], oldPos[1]))
		self.trace.append((newPos[0], newPos[1]))
		return self	

	def isGoalState(self):
		#########################################
		# check for Goal State: Goal state is when center is a peg 
		# and all other positions are not having peg
		########################################
		
		dim = len(self.gameState)
		
		if(self.gameState[(dim - 1)/2][(dim - 1)/2] != 1):
			return False
		else:
			for i in range(dim):
				for j in range(dim):
					if( i == (dim - 1)/2 and j == (dim - 1)/2):
						continue
					elif( self.gameState[i][j] == 1):	
						return False
		return True


	def backTrackGameState(self, oldPos, direction):
		#########################################
		#########################################
		# Backtrack to the previous Game State:
		#########################################
		#########################################

		# Set the peg of old position again #
		self.gameState[oldPos[0]][oldPos[1]] = 1
		
		# Set the peg of intermediate position again #
		interPos = self.getIntermediatePosition(oldPos, direction)
		self.gameState[interPos[0]][interPos[1]] = 1

		# Reset the peg of final position again #				
		newPos = self.getIntermediatePosition(interPos, direction)
		self.gameState[newPos[0]][newPos[1]] = 0

		return True

	def isPegAtPos(self, pos):
		#########################################
		#########################################
		# Check if current position contains peg:
		#########################################
		#########################################
		if(self.gameState[pos[0]][pos[1]] == 1):
			return True
		else:
			return False 	
	
