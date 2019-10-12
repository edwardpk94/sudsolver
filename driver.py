import os
import sys
import sudsolver

puzzles_dir = './data/puzzles/'
solutions_dir = './data/solutions/'

if (not os.path.isdir(puzzles_dir) or not os.path.isdir(solutions_dir)):
    print("either puzzles or solutions directory does not exist")
    sys.exit(1)

puzzle_files = os.listdir(puzzles_dir)
solution_files = [os.path.splitext(puzzle_file)[0] + '_s.txt' for puzzle_file in puzzle_files]

puzzle_paths = [os.path.join(puzzles_dir, puzzle_file) for puzzle_file in puzzle_files]
solution_paths = [os.path.join(solutions_dir, solution_file) for solution_file in solution_files]

# print(puzzle_paths)
print(solution_paths)

# print(sudsolver.read(puzzle_paths[0]))

# solution_path = os.puzzle_name + '_s.txt' + solution_paths

# test_puzzle = sudsolver.read(puzzle_path)
# test_solution = sudsolver.read(solution_path)
# sudsolver.print_board(test_puzzle)
# sudsolver.print_board(test_solution)


# puzzles = [sudsolver.read(puzzle_path) for puzzle_path in puzzle_paths]
# for puzzle in puzzles:
#     sudsolver.print_board(puzzle)
#     print('')

solution = sudsolver.read(solution_paths[0])
print(solution)
# solutions = [sudsolver.read(solution_path) for solution_path in solution_paths]
#
# for puzzle in puzzles:
#     sudsolver.print_board(puzzle)

#for puzzle_file in puzzle_paths:
    #sudsolver.read(puzzles_dir + puzzle_file)
    #with puzzle as
    #puzzles.append()