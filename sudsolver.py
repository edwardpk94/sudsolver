import sys
import os

def read(file_name):
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


#def solve():

def print_board(board):
    for row in board:
        print(row)

def compare_boards(board1, board2):
    if (board1 == board2):
        return True
    return False