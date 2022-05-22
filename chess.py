#!/usr/bin/python -tt
import os
import numpy as np

# Clear the terminal
os.system('clear')

# Define the chess board where 1 represents a Queen and 0 represents an unoccuppied square

# Automatically create list
board= np.zeros((8,8),dtype=type(1))
#print(board)
    # Generate flat nondiagonal indices using masking
idx = np.flatnonzero(~np.eye(8,dtype=bool))
#print("idx", idx)
    # Select num_rand random indices from those and set those
    # in a flattened view of the array to be as fillval
board.ravel()[np.random.choice(idx, 2, replace=0)] = 1
print(board)
grid_size = len(board)
# test = board.tolist()
# print(test)
locations = []
def main():
    count_queen = 0
  # Get the position of the queens
    for row in range(0, grid_size, 1):
        for column in range(0, grid_size, 1):
          # If the value of the square is 1 Queen is loacted
            if board[row][column] == 1:
                print("Queen", count_queen, "here in row",  row, "and at",  "column", column)
                locations.append([count_queen, row, column])
                count_queen =+ 1
    
    if locations[0][1] == locations[1][1]:
      print("Threat on the same row")
    elif locations[0][2] == locations[1][2]:
        print("Threat on the same column")
         # Diagonal test needs work
    elif ((locations[0][1] - locations[1][1]) == 0 and (locations[0][2] - locations[1][2]) == 0) or \
          ((locations[1][1] -locations[0][1]) == 0 and (locations[1][2] - locations[0][2]) == 0): 
          print("Threat on an diagonal")
    else:
      print("No threat detected")


    
    # Check for contact in row and diagonals


    


                
   
  # Print if can take the other Queen

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()