# sudsolver
A sudoku module. Reads and solves sudokus

# Usage
import sudsolver

puzzles = sudsolver.read_single_lines('/path/to/file/.txt')

for puzzle in puzzles:
  solution = sudsolver.solve(puzzle)
  
# License
Creative Commons BY-NC-SA 4.0
more info at https://creativecommons.org/licenses/by-nc-sa/4.0/
