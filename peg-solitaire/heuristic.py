import pegSolitaireUtils
import config
import readGame

def heuristicOneManhattan(pegSolitaireObject):
	#################################################
    #################################################
    # Using Manhattan distance which in this case sum of absolute differences of x 
    # and y for various peg  positions to center position
    #################################################
    hCost = 0
    dim = len(pegSolitaireObject.gameState)
    for i in range(dim):
    	for j in range(dim):
    		if(pegSolitaireObject.isPegAtPos((i,j)) == True):
				cost = abs(i - ((dim - 1)/2)) + abs(j - ((dim - 1)/2))
				hCost = hCost + cost
	return hCost

def heuristicTwoWeightedCost(pegSolitaireObject):
	#################################################
    #################################################
    # Using weight of each peg position based on its location in the grid
    # weights suggest whether chances of reaching to a goal are higher with 
    # this state or not
    #Reference: Barker, Joseph K., and Richard E. Korf. Solving Peg Solitaire with 
    #Bidirectional BFIDA.
    #################################################
    hCost = 0
    weightCost = [[0,0,-1,0,1,0,0],
                  [0,0,1,1,1,0,0],
                  [-1,1,0,1,0,1,-1],
                  [0,1,1,0,1,1,0],
                  [-1,1,0,1,0,1,-1],
                  [0,0,1,1,1,0,0],
                  [0,0,-1,0,1,0,0]]              
    dim = len(pegSolitaireObject.gameState)
    for i in range(dim):
    	for j in range(dim):
    		if(pegSolitaireObject.isPegAtPos((i,j)) == True):
				hCost = hCost + weightCost[i][j]
	return hCost
    