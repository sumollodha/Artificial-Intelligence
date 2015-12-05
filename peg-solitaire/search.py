import pegSolitaireUtils
import config
import readGame
import copy
import heuristic
import Queue as Q

##Keeping corner box dimenions here for easy changes
cornerBoxDimensions = (2,2)

def ItrDeepSearchUtil(pegSolitaireObject,depth):
	#################################################
    #################################################
    # Utility function which generate next successor for ITR deepening search
    #based on the depth given, tries to find the result in that depth range
    #################################################
    #################################################
	if(depth<0):
		return False
	if(pegSolitaireObject.isGoalState()):
		readGame.trace = pegSolitaireObject.trace
		return True
		
	dim = len(pegSolitaireObject.gameState)

	for i in range(dim):
		for j in range(dim):
			keys = config.DIRECTION.keys()
			if (pegSolitaireObject.isPegAtPos((i,j)) == False):
				continue
			for k in range(len(keys)):
				direction = keys[k]
				if(pegSolitaireObject.is_validMove((i,j), direction)):
					copyPegSolitaireObject = copy.deepcopy(pegSolitaireObject)
					newPegSolitaireObject = copyPegSolitaireObject.getNextState((i,j), direction)
 					if(pegSolitaireObject.gameState[i][j] != newPegSolitaireObject.gameState[i][j]):
 						if(ItrDeepSearchUtil(newPegSolitaireObject,depth - 1) == True):
 							return True
	return False		


def ItrDeepSearch(pegSolitaireObject):
	#################################################
	# Must use functions:
	# getNextState(self,oldPos, direction)
	# 
	# we are using this function to count,
	# number of nodes expanded, If you'll not
	# use this grading will automatically turned to 0
	#################################################
	#
	# using other utility functions from pegSolitaireUtility.py
	# is not necessary but they can reduce your work if you 
	# use them.
	# In this function you'll start from initial gameState
	# and will keep searching and expanding tree until you 
	# reach goal using Iterative Deepning Search.
	# you must save the trace of the execution in pegSolitaireObject.trace
	# SEE example in the PDF to see what to save
	#
	#################################################

	## Getting dimenions of GameState matrix and corner matrix##
	nRows = len(pegSolitaireObject.gameState)
	nCols = len(pegSolitaireObject.gameState[0])
	totalBlocks = nRows * nCols
	totalCorners = 4*cornerBoxDimensions[0]*cornerBoxDimensions[1]
	## Running DFS iteratively for each depth ##
	startPos = pegSolitaireObject.gameState
	for depth in range(totalBlocks - totalCorners):
		if(ItrDeepSearchUtil(pegSolitaireObject, depth+1) == True):
			pegSolitaireObject.trace = readGame.trace
			pegSolitaireObject.nodesExpanded = readGame.totalNodeExpended
			return True
	return False

def aStarOne(pegSolitaireObject):
	#################################################
    #################################################
    #
    # using other utility functions from pegSolitaireUtility.py
    # is not necessary but they can reduce your work if you 
    # use them.
    # In this function you'll start from initial gameState
    # and will keep searching and expanding tree until you 
	# reach goal using A-Star searching with first Heuristic
	# you used.
    # you must save the trace of the execution in pegSolitaireObject.trace
    # SEE example in the PDF to see what to return
    #
    #################################################
    readGame.totalNodeExpended = 0
    ## Getting dimenions of GameState matrix ##
    dim = len(pegSolitaireObject.gameState)
    h = 0
    f = 0
    ##creating the Priority queue
    q = Q.PriorityQueue()
    q.put((0,pegSolitaireObject))
    currPegSolitaireObject = pegSolitaireObject
    isGoalReached = currPegSolitaireObject.isGoalState()
    ##Iteration over the elements in Priority queue
    while(q.empty() == False):
		currPegSolitaireObject = q.get()[1]
		isGoalReached = currPegSolitaireObject.isGoalState()
		if(isGoalReached == True):
			break
		for i in range(dim):
			for j in range(dim):
				keys = config.DIRECTION.keys()
				if (currPegSolitaireObject.isPegAtPos((i,j)) == False):
					continue
				for k in range(len(keys)):
					direction = keys[k]					
					if(currPegSolitaireObject.is_validMove((i,j), direction)):
						copyPegSolitaireObject = copy.deepcopy(currPegSolitaireObject)
						newPegSolitaireObject = copyPegSolitaireObject.getNextState((i,j), direction)
						newPegSolitaireObject.g = newPegSolitaireObject.g + 1
						if(currPegSolitaireObject.gameState[i][j] != newPegSolitaireObject.gameState[i][j]):
							h = heuristic.heuristicOneManhattan(newPegSolitaireObject)						
							f = newPegSolitaireObject.g + h
							q.put((h, newPegSolitaireObject))
    if(isGoalReached == True):
		pegSolitaireObject.trace = currPegSolitaireObject.trace
		pegSolitaireObject.nodesExpanded = readGame.totalNodeExpended
		return True
    else:
		return False	

def aStarTwo(pegSolitaireObject):
	#################################################
    # Must use functions:
    # getNextState(self,oldPos, direction)
    # 
    # we are using this function to count,
    # number of nodes expanded, If you'll not
    # use this grading will automatically turned to 0
    #################################################
    #
    # using other utility functions from pegSolitaireUtility.py
    # is not necessary but they can reduce your work if you 
    # use them.
    # In this function you'll start from initial gameState
    # and will keep searching and expanding tree until you 
    # reach goal using A-Star searching with second Heuristic
    # you used.
    # you must save the trace of the execution in pegSolitaireObject.trace
    # SEE example in the PDF to see what to return
    #
    #################################################        
    readGame.totalNodeExpended = 0
    ## Getting dimenions of GameState matrix ##
    dim = len(pegSolitaireObject.gameState)
    h = 0
    f = 0    
    ##creating the Priority queue
    q = Q.PriorityQueue()
    q.put((0,pegSolitaireObject))
    currPegSolitaireObject = pegSolitaireObject
    isGoalReached = currPegSolitaireObject.isGoalState()
    ##Iteration over the elements in Priority queue
    while(q.empty() == False):
		currPegSolitaireObject = q.get()[1]
		#print "get from queue"
		isGoalReached = currPegSolitaireObject.isGoalState()
		if(isGoalReached == True):
			break
		for i in range(dim):
			for j in range(dim):
				keys = config.DIRECTION.keys()
				if (currPegSolitaireObject.isPegAtPos((i,j)) == False):
					continue
				for k in range(len(keys)):
					direction = keys[k]					
					if(currPegSolitaireObject.is_validMove((i,j), direction)):
						copyPegSolitaireObject = copy.deepcopy(currPegSolitaireObject)
						newPegSolitaireObject = copyPegSolitaireObject.getNextState((i,j), direction)
						newPegSolitaireObject.g = newPegSolitaireObject.g + 1
						if(currPegSolitaireObject.gameState[i][j] != newPegSolitaireObject.gameState[i][j]):
							h = heuristic.heuristicTwoWeightedCost(newPegSolitaireObject)						
							f = newPegSolitaireObject.g + h
							q.put((f, newPegSolitaireObject))
    if(isGoalReached == True):
		pegSolitaireObject.trace = currPegSolitaireObject.trace
		pegSolitaireObject.nodesExpanded = readGame.totalNodeExpended
		return True
    else:
		return False	