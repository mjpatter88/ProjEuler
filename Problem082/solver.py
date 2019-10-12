# NOTE: This problem is a more challenging version of Problem 81.
#
# The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the
# left column and finishing in any cell in the right column, and only moving up,
# down, and right, is indicated in red and bold; the sum is equal to 994.
#
# 131 673 234 103 18
# 201  96 342 965 150
# 630 803 746 422 111
# 537 699 497 121 956
# 805 732 524  37 331
#
# 201 -> 96 -> 342 -> 234 -> 103 -> 18
#
# Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."),
# a 31K text file containing a 80 by 80 matrix, from the left column to the right column.
#

# Algorithmic approach thoughts: Same as Problem 81, just 5 possible starting positions
# and three possible moves.
# Recursive, dynamic programming most likely will be a good fit.
# Could also try something like djikstra's alg.
#
# One wrinkle is that you can go up or down, so I'll have to handle backtracking to prevent
# infinite recursion. This also means my cache will have to be keyed off that as well.

# (row, col, prev_move) -> answer
cache ={}

from enum import Enum, auto

class Move(Enum):
    RIGHT = auto()
    UP = auto()
    DOWN = auto()

def read_input(file):
    matrix = []
    for line in file:
        matrix.append([int(entry) for entry in line.strip().split(",")])
    width = len(matrix[0])
    for row in matrix:
        assert len(row) == width

    return matrix

def min_path_sum(matrix, row, col, prev_move):
    # We have to be careful to avoid backtracking which could result in
    # infinite recursion. For this reason, we take in prev_move, so we 
    # can prevent up -> down and down -> up combos.
    if (row, col, prev_move) in cache:
        return cache[(row, col, prev_move)]
    max_row = len(matrix) - 1
    max_col = len(matrix[0]) - 1
    answer = None
    if col == max_col:
        answer = matrix[row][col]
    elif row == 0:
        possible_moves = [min_path_sum(matrix, row, col+1, Move.RIGHT)]
        if prev_move != Move.UP: # only move down if we have't just moved up.
            possible_moves.append(min_path_sum(matrix, row+1, col, Move.DOWN))
        answer = matrix[row][col] + min(possible_moves)
    elif row == max_row:
        possible_moves = [min_path_sum(matrix, row, col+1, Move.RIGHT)]
        if prev_move != Move.DOWN: # only move up if we have't just moved down.
            possible_moves.append(min_path_sum(matrix, row-1, col, Move.UP))
        answer = matrix[row][col] + min(possible_moves)
    else:
        # We can always move right since LEFT is not a possible move
        possible_moves = [min_path_sum(matrix, row, col+1, Move.RIGHT)]
        if prev_move != Move.UP: # only move down if we have't just moved up.
            possible_moves.append(min_path_sum(matrix, row+1, col, Move.DOWN))
        if prev_move != Move.DOWN: # only move up if we have't just moved down.
            possible_moves.append(min_path_sum(matrix, row-1, col, Move.UP))
        answer = matrix[row][col] + min(possible_moves)
    cache[(row, col, prev_move)] = answer
    return answer

def min_path_total(matrix):
    # If we want to support multiple calls, we must reset the cache each time.
    global cache
    cache = {}

    possibles = [min_path_sum(matrix, row, 0, None) for row in range(len(matrix))]
    return min(possibles)

def solve(filename):
    with open(filename) as in_file:
        mat = read_input(in_file)
    return min_path_total(mat)

if __name__ == '__main__':
    print(solve("matrix.txt"))
