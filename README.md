# sudsolver
A sudoku moduel. Reads and solves sudokus

#Usage
import sudsolver

puzzles = sudsolver.read_single_lines('/path/to/file/.txt')

for puzzle in puzzles:
  solution = sudsolver.solve(puzzle)
