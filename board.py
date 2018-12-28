# Gurjaspal Singh Bedi
# Intelligent Systems and Engineering, Indiana University

#!/usr/bin/env python
import sys
import numpy as np


# Declaring Problem Types
class ProblemType:
    NQUEEN = 'nqueen'
    NKNIGHT = 'nknight'
    NROOK = 'nrook'

# Declaring the symbols that must be used for particular problem  type
class Symbols:
    NQUEEN = 'Q'
    NKNIGHT = 'K'
    NROOK = 'R'
    BLOCKED = 'X'
    BLANK = '_'


pt = ProblemType()
symbol = Symbols()


# Count # of pieces in given row
def count_on_row(board, row):
    return sum(board[row])


# Count # of pieces in given column
def count_on_col(board, col):
    return sum([row[col] for row in board])


# Count total # of pieces on board
def count_pieces(board):
    return sum([ sum(row) for row in board ] )


# Returns if diagonal has queen already or not
# Following line of code has been taken from
# #https://stackoverflow.com/questions/46135906/pythonic-way-to-get-the-diagonals-passing-through-a-point-x-y
def has_no_queen_diagonal(board, r, c):
    return sum(np.diagonal(board, offset=(c - r))) == 0


# Return if anti-diagonal has queen already or not
# Following line of code has been taken from
# #https://stackoverflow.com/questions/46135906/pythonic-way-to-get-the-diagonals-passing-through-a-point-x-y
def has_no_queen_antidiagonal(board, r, c):
    return sum(np.diagonal(np.rot90(board), offset=-board.shape[1] + (c + r) + 1)) == 0

# This function tests if it is fine to place the knight at r row and c column
def safe_to_place_knight(board, r, c):
    points_of_attack = []
    points_of_attack.append([r + 2, c - 1])
    points_of_attack.append([r + 2, c + 1])
    points_of_attack.append([r - 2, c - 1])
    points_of_attack.append([r - 2, c + 1])
    points_of_attack.append([r + 1, c + 2])
    points_of_attack.append([r + 1, c - 2])
    points_of_attack.append([r - 1, c + 2])
    points_of_attack.append([r - 1, c - 2])
    list_knight= []
    for point in points_of_attack:
        if point[0] < N and point[0] >=0 and point[1] < N and point[1] >= 0:
            list_knight.append(point)

    for item in list_knight:
        return not (board[item[0]][item[1]] == 1)


# Function to get the symbol to display the board
def get_board_icon(board, r, c):

    if [r+1,c+1] in blockers_points:
        return symbol.BLOCKED
    if board[r][c] == 0:
        return symbol.BLANK
    if problemType == pt.NROOK:
        return symbol.NROOK
    else:
        if problemType == pt.NQUEEN:
            return symbol.NQUEEN
        else:
            if problemType == pt.NKNIGHT:
                return Symbols.NKNIGHT
            else:
                print("Wrong problem type")
                return "W"


def is_not_a_blocking_point(board, r, c):
    return [r+1, c+1] not in blockers_points


# Return a string with the board rendered in a human-friendly format
def printable_board(board):
    return "\n".join([ " ".join([ get_board_icon(board, rowIndex,colIndex) for colIndex, col in enumerate(row) ]) for rowIndex, row in enumerate(board)])


# Add a piece to the board at the given position, and return a new board (doesn't change original)
def add_piece(board, row, col):
    return board[0:row] + [board[row][0:col] + [1,] + board[row][col+1:]] + board[row+1:]


def conditions_for_queens(board, r, c):
    if problemType == pt.NQUEEN:
        numpy_board = np.array(board)
        return has_no_queen_diagonal(numpy_board, r, c) and has_no_queen_antidiagonal(numpy_board, r, c)
    return True


# Get list of successors of given board state
def successors(board):
    succ_list = []
    piecesOnBoard = count_pieces(board)

    for r in range(0,N):
            for c in range(0,N):
                if problemType == pt.NKNIGHT:
                    if board[r][c] == 0 and piecesOnBoard < N and safe_to_place_knight(board, r, c) and is_not_a_blocking_point(board,r,c):
                        succ_list.append(add_piece(board, r, c))
                elif board[r][c] == 0 and piecesOnBoard < N and count_on_row(board,r) == 0 and is_not_a_blocking_point(board,r,c) and count_on_col(board,c) == 0 and conditions_for_queens(board,r,c):
                        succ_list.append(add_piece(board, r, c))
            if len(succ_list) > 0:
                return succ_list
    return succ_list

def is_goal(board):

    if problemType == pt.NKNIGHT:
        return count_pieces(board) == N
    else:
        return count_pieces(board) == N and \
               all([count_on_row(board, r) <= 1 for r in range(0, N)]) and \
               all([count_on_col(board, c) <= 1 for c in range(0, N)])


# Get board with the blocking points
def board_with_blocking_points(board, points):
    for item in points:
        board[int(item[0])][int(item[1])] = 'X'
    return board


# Solve n-rooks,n-queen or n-knights!
def solve(initial_board):
    fringe = [initial_board]
    while len(fringe) > 0:
        popElement = fringe.pop()
        my_list = successors( popElement )
        for s in my_list:
                if is_goal(s):
                    return(s)
                fringe.append(s)
    return False


# Reading the problem type from the arguments
problemType = sys.argv[1]

# Reading the size of the board
N = int(sys.argv[2])

# Empty list to store all the points
blockers_points =[]

# Condition if no blockers are given
if len(sys.argv) > 3:
    blockers_count = sys.argv[3]
    for t in range (4, len(sys.argv),2):
        blockers_points.append([int(sys.argv[t]),int(sys.argv[t+1])])
else:
    blockers_count = 0


# The board is stored as a list-of-lists. Each inner list is a row of the board.
# A zero in a given square indicates no piece, and a 1 indicates a piece.
initial_board = [[0]*N]*N

solution = solve(initial_board)
print(printable_board(solution) if solution else "Sorry, no solution found. :(")


