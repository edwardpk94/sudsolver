# Copyright Edward Kunkel 2019
# Released to the public under CC BY-NC-SA 4.0
# more info at https://creativecommons.org/licenses/by-nc-sa/4.0/

import os
import sys
import sudsolver

puzzles_dir = './data/MultiArrayStyle/puzzles/'
solutions_dir = './data/MultiArrayStyle/solutions/'

if (not os.path.isdir(puzzles_dir) or not os.path.isdir(solutions_dir)):
    print("either puzzles or solutions directory does not exist")
    sys.exit(1)

puzzle_files = os.listdir(puzzles_dir)
solution_files = [os.path.splitext(puzzle_file)[0] + '_s.txt' for puzzle_file in puzzle_files]

puzzle_paths = [os.path.join(puzzles_dir, puzzle_file) for puzzle_file in puzzle_files]
solution_paths = [os.path.join(solutions_dir, solution_file) for solution_file in solution_files]

puzzles = sudsolver.read_single_lines('./data/LinePerPuzzleStyle/0.txt')

for puzzle in puzzles:
    # print('printing puzzle:')
    # sudsolver.print_board(puzzle)
    solution = sudsolver.solve(puzzle)
    # print('printing solution:')
    # sudsolver.print_board(solution)

print('solved ' + str(len(puzzles)) + ' puzzles!')