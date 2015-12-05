from util import memoize, run_search_function
from util import NEG_INFINITY

def basic_evaluate(board):
    """
    The original focused-evaluate function from the lab.
    The original is kept because the lab expects the code in the lab to be modified. 
    """
    if board.is_game_over():
        # If the game has been won, we know that it must have been
        # won or ended by the previous move.
        # The previous move was made by our opponent.
        # Therefore, we can't have won, so return -1000.
        # (note that this causes a tie to be treated like a loss)
        score = -1000
    else:
        score = board.longest_chain(board.get_current_player_id()) * 10
        # Prefer having your pieces in the center of the board.
        for row in range(6):
            for col in range(7):
                if board.get_cell(row, col) == board.get_current_player_id():
                    score -= abs(3-col)
                elif board.get_cell(row, col) == board.get_other_player_id():
                    score += abs(3-col)

    return score


def get_all_next_moves(board):
    """ Return a generator of all moves that the current player could take from this position """
    from connectfour import InvalidMoveException

    for i in xrange(board.board_width):
        try:
            yield (i, board.do_move(i))
        except InvalidMoveException:
            pass

def is_terminal(depth, board):
    """
    Generic terminal state check, true when maximum depth is reached or
    the game has ended.
    """
    return depth <= 0 or board.is_game_over()

def minimax_util(board, depth, eval_fn, get_next_moves_fn,
                        is_terminal_fn,max_index):
    """using negmax varient of minmax algorithm"""
    if(depth <= 0):
        """using pow of depth instaed of passing an extra argument"""
        return (pow(-1, depth)* eval_fn(board))
    currentUtil = NEG_INFINITY
    for i,new_board in get_next_moves_fn(board):
        if(is_terminal_fn(depth, new_board) != True):
            utilVal = -minimax_util(new_board, depth -1, eval_fn, get_next_moves_fn,
                    is_terminal_fn,max_index)
            if(currentUtil < utilVal):
                currentUtil = utilVal
                """removing the previous max index and saving current one"""
                if max_index:
                    max_index.pop(0)
                max_index.insert(0,i)
    return currentUtil

def minimax(board, depth, eval_fn = basic_evaluate,
            get_next_moves_fn = get_all_next_moves,
            is_terminal_fn = is_terminal,
            verbose = True):
    """
    Do a minimax search to the specified depth on the specified board.

    board -- the ConnectFourBoard instance to evaluate
    depth -- the depth of the search tree (measured in maximum distance from a leaf to the root)
    eval_fn -- (optional) the evaluation function to use to give a value to a leaf of the tree; see "focused_evaluate" in the lab for an example

    Returns an integer, the column number of the column that the search determines you should add a token to
    """
    max_index = []
    max_util = minimax_util(board, depth, eval_fn, get_next_moves_fn,
                    is_terminal_fn,max_index)
    column = 0
    """max index will have the column in which nect move need to be occured"""
    if max_index:
        column = max_index.pop(0)
    return column

def rand_select(board):
    """
    Pick a column by random
    """
    import random
    moves = [move for move, new_board in get_all_next_moves(board)]
    return moves[random.randint(0, len(moves) - 1)]

def check_digonals(board):
    sum = 0
    ###cheking if opponent is going to win ###
    for sum in range(board.board_width + board.board_height - 2):
        count = 0
        for i in range(board.board_width):
            for j in range(board.board_height):
                if (i + j - sum == 0):
                    if(playerid == board.get_cell(row, col)):
                        count = count + 1
                        if(count == board.get_current_winning_k()):
                            return True
                    else:
                        count = 0
    return False

def add_weightage_of_center(board,score):
#Adding weigtage for center
    for row in range(board.board_height):
        for col in range(board.board_width):
            if board.get_cell(row, col) == board.get_current_player_id():
                score -= abs(3-col)
            elif board.get_cell(row, col) == board.get_other_player_id():
                score += abs(3-col)
    return score

def new_evaluate(board):
    score = 0
    k=board.get_current_winning_k()
    if board.is_game_over():
        # If the game has been won, we know that it must have been
        # won or ended by the previous move.
        # The previous move was made by our opponent.
        # Therefore, we can't have won, so return -1000.
        # (note that this causes a tie to be treated like a loss)
        score = -1000
    else:
        """ Score calcuation for current player longest chain length """
        score = board.longest_chain(board.get_current_player_id()) * 12
        """ Now checking for other other player positions for blocking his win move """
        #rows checking
        for row in range(board.board_height):
            for col in range(board.board_width - k + 1):
                start = col
                st =0
                for start in range(col+k-2):
                    #print "col",col, "start",start
                    if(board.get_cell(row, start) == board.get_other_player_id()):
                        continue
                    else:
                        st=start
                        #print "hi"
                        break
                if(st != col+k-2):
                    continue;        
                elif(col-1 >=0 and board.get_cell(row, col-1) == board.get_current_player_id()):
                    score += ((k)*10)
                elif(st < board.board_width and board.get_cell(row, st+1) == board.get_current_player_id()):
                    score += ((k)*10)
        score = add_weightage_of_center(board,score)
        return score
        
        #cols checking
        for col in range(board.board_height):
            for row in xrange(5,k-2,-1):
                for start in xrange(row,row-k+2,-1):
                    if(board.get_cell(start, col) == board.get_other_player_id()):
                        continue
                    else:
                        break
                if(start != col+k-2):
                    continue;        
                elif(start-1 >=0 and board.get_cell(start-1, col) == board.get_current_player_id()):
                    score += (k-1)*10
        score = add_weightage_of_center(board,score)
        return score

        #digonals checking
        if(check_digonals(board) == True):
            score += (k-1)*10
            score = add_weightage_of_center(board,score)
            return score
    score = add_weightage_of_center(board,score)
    return score

random_player = lambda board: rand_select(board)
#########################################
############Execution Time: 54.3500454486
############Nodes Expanded: 28214
##########################################
basic_player = lambda board: minimax(board, depth=4, eval_fn=basic_evaluate)
#########################################
############Execution Time: 54.3500454486
############Nodes Expanded: 28214
##########################################
new_player = lambda board: minimax(board, depth=4, eval_fn=new_evaluate)
progressive_deepening_player = lambda board: run_search_function(board, search_fn=minimax, eval_fn=basic_evaluate)
