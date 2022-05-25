#!/usr/bin/python -tt
import os
# generate random integer values
from random import seed
from random import randint
import numpy as np

# Clear the terminal
os.system('clear')

# Define the chess board where 1 represents a Queen and 0 represents an unoccuppied square

# Automatically create list
board = []
size_board = 8
for i in range(size_board):
    board.append([])
    for j in range(size_board):
        board[i].append(0)

    # Add the Queens
for queen in range(0, 2, 1):
    row = randint(0, 7)
    column = randint(0, 7)
    if board[row][column] != 1:
        board[row][column] = 1
        queen = + 1
arr = np.array(board)
print(arr)

grid_size = len(board)
print(grid_size)
# test = board.tolist()
# print(test)
locations = []


def main():
    count_queen = 0
    # Get the position of the queens
    for row in range(0, grid_size, 1):
        for column in range(0, grid_size, 1):
            # If the value of the square is 1 Queen is located

            if board[row][column] == 1:
                print("Queen", count_queen, "here in row", row, "and at", "column", column)
                locations.append([count_queen, row, column])
                count_queen = count_queen + 1
    print("Queen location", locations)
 
    if locations[0][1] == locations[1][1]:
        print("Threat on the same row")
    elif locations[0][2] == locations[1][2]:
        print("Threat on the same column")
    # Diagonal test needs work
    
    elif (abs(locations[0][1] - locations[1][1]) - abs(locations[0][2] - locations[1][2])) == 0:
        print("Threat on an diagonal")
    else:
        print("No threat detected")


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
