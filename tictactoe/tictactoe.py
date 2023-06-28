"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """ 
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """ 
    # if game is over, return any
    if terminal(board) == True:
        return None        

    count_x = 0
    count_o = 0
    for row in board:
        count_x += row.count(X)
        count_o += row.count(O)  
    
    # if X is on the board more than O, O's turn
    if count_x > count_o:
        return O
    
    # if the remainder of the count of X and O = 0, it's X's turn again
    if (count_x + count_o) % 2 == 0:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # if game is over, return any
    # if terminal(board):
    #     return set()  

    # add available moves to set
    action = set()

    # return all the moves, (i,j), where i is row and j is column 
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action.add((i, j))

    return action            


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # board copy
    board_copy = deepcopy(board)
    i, j = action

    # update board after making move
    if player(board_copy) == X:
        board_copy[i][j] = X
    elif player(board_copy) == O:
        board_copy[i][j] = O            
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # if X or O has three in a row, return the winner
    for row in board:
        if row[0] == row[1] == row[2] == X:
            return X
        elif row[0] == row[1] == row[2] == O:
            return O
        
    # if X or O has three in a row down a colum, return the winner     
    for field in range(3):
        if board[0][field] == board[1][field] == board[2][field] == X:
            return X
        elif board[0][field] == board[1][field] == board[2][field] == O:
            return O
        
    # if there are three in a row down the diagonals:
    if board[0][0] == board[1][1] == board[2][2] == X:
        return X
    elif board[0][0] == board[1][1] == board[2][2] == O:
        return O    
    elif board[2][0] == board[1][1] == board [0][2] == X:
        return X
    elif board[2][0] == board[1][1] == board [0][2] == O:
        return O      
        
    return None
       

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # if either player has won
    if winner(board) == X or winner(board) == O:    
        return True   

    # if no more moves left
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False       
    return True     


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:   
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """        
    if terminal(board):
        return None      
       
    for action in actions(board):
        if player(board) == X:
            # MAX picks action a in actions(s) that produces highest value of min-value(result(s,a))
            if max_value(board) == min_value(result(board, action)):
                return action
        else:
            # MIN picks action a in actions(s) that produces smallest value of min-value(result(s,a))
            if min_value(board) == max_value(result(board, action)):
                return action
        
    
def max_value(board):  
    """
    Returns max value of any given board
    """           
    if terminal(board) == True:
        return utility(board)
    v = -math.inf  
    for action in actions(board):
        v = max(v, min_value(result(board, action)))            
    return v
    

def min_value(board):
    """
    Returns min value of any given board
    """
    if terminal(board) == True:
        return utility(board)
    v = math.inf   
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v



