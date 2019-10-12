# Copyright Edward Kunkel 2019
# Released to the public under CC BY-NC-SA 4.0
# more info at https://creativecommons.org/licenses/by-nc-sa/4.0/

import sys
import os
from collections import namedtuple

VERIFICATION_SET = {1,2,3,4,5,6,7,8,9}

#read a puzzle with each line representing a row of the board
def read_multi_line(file_name):
    """Read a text file containing one puzzle, specified 9 entries per line

    :param file_name: The file to be read
    :return: The puzzle as a list of lists of integers
    """

    if (not os.path.isfile(file_name)):
        print(f"file_name {file_name} does not exist. Exiting program")
        sys.exit(1)

    with open(file_name,mode="r") as file:
        board = []
        for line in file:
            if (line.strip()):
                row = [int(num) for num in line.split()]
                board.append(row)
        return board

def read_single_lines(file_name: str):
    """Read a file whose lines each represent a puzzle.

    :param file_name: The file to be read
    :return: A list of puzzles, each of which is a list of list of integers
    """

    if (not os.path.isfile(file_name)):
        print(f"file_name {file_name} does not exist. Exiting program")
        sys.exit(1)

    with open(file_name,mode="r") as file:
        boards = []
        for line in file:
            if (line.strip()):
                board = []
                row = []
                for char_num,char in enumerate(line.rstrip()):
                    num = int(char)
                    row.append(num)
                    if ((char_num+1) % 9) == 0:
                        board.append(row)
                        row = []
                boards.append(board)
        return boards

def solve(board):
    """Solve a sudoku puzzle and return the solution.

    :param board: The sudoku puzzle as a list of list of integers
    :return: The solved sudoku
    """

    #copy the board so the original isn't overwritten
    solution = board
    __solve_encapsulated(solution,0,0)

    if not verify_board(solution):
        print('ERROR: Solution was attempted but is not verified')
        sys.exit(1)

    return solution

def __solve_encapsulated(board,rowDx=0,colDx=0):
    """Internal method used to solve sudoku.

    :param board: The sudoku puzzle as a list of list of integers
    :params rowDx, colDx: The location to begin solving the board
    :return: Whether the function successfully solved the sudoku
    """

    rowDx, colDx, found_entry = __next_empty_entry(board,rowDx,colDx)

    if not found_entry:
        return True
    
    for possible_num in range(1,10):
        if __check_entry(board, possible_num, rowDx, colDx):
            board[rowDx][colDx] = possible_num
            if __solve_encapsulated(board, rowDx, colDx):
                return True

    board[rowDx][colDx] = 0
    return False

def print_board(board):
    """Print the sudoku and a newline"""

    for row in board:
        print(row)
    print('\n')

def __check_row(board,num,rowDx) -> bool:
    """Check if a number exists in a row"""

    for entry in board[rowDx]:
        if num == entry:
            return False
    return True


def __check_col(board,num,colDx) -> bool:
    """Check if a number exists in a column"""

    for row in board:
        if num == row[colDx]:
            return False
    return True

def __check_square(board, num, rowDx, colDx) -> bool:
    """Check if a number exists in a position's 'square'"""

    square_rowDx = rowDx // 3
    square_colDx = colDx // 3
    for row in board[square_rowDx*3:(square_rowDx*3+3)]:
        for entry in row[square_colDx*3:(square_colDx*3+3)]:
            if entry == num:
                return False
    return True

def __check_entry(board, num, rowDx, colDx) -> bool:
    """Check if a specified number does not violate the current puzzle"""

    return (__check_row(board,num,rowDx)
        and __check_col(board,num,colDx)
        and __check_square(board,num,rowDx,colDx))


def __next_empty_entry(board, rowDx, colDx):
    """Obtain the next empty entry in the puzzle"""

    for i,row in enumerate(board[rowDx:9]):
        for j,entry in enumerate(row[colDx:9]):
            if entry == 0:
                return (i+rowDx,j+colDx,True)

        #only search from the specified column in first row.
        #Afterwards must search all of each row
        colDx = 0

    return (0,0,False)

def verify_board(board):
    """Verify that a board is correctly solved"""

    current_set = set()
    #check all entries in each row
    for row in board:
        for entry in row:
            current_set.add(entry)

        if current_set != VERIFICATION_SET:
            print(current_set)
            print(VERIFICATION_SET)
            print('rows didnt match')
            return False
        current_set.clear()

    #check all entries in each column
    for colDx in range(9):
        for row in board:
            current_set.add(row[colDx])

        if current_set != VERIFICATION_SET:
            print('ERROR: at least one columnb did not pass verification')
            return False
        
    #check all entries in each square
    for square_rowDx in range(3):
        for square_colDx in range(3):
            if not verify_square(board, square_rowDx, square_colDx):
                print('ERROR:  didnt match during board verification')
                return False

    return True

def verify_square(board, square_rowDx, square_colDx):
    """Verify that a specified 3x3 'square' in a puzzle is solved correctly"""

    current_set = set()
    for row in board[square_rowDx*3:(square_rowDx*3+3)]:
        for entry in row[square_colDx*3:(square_colDx*3+3)]:
            current_set.add(entry)

    if current_set != VERIFICATION_SET:
        return False
    
    return True
