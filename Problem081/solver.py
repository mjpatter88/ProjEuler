# In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.
#
# 131 673 234 103 18
# 201  96 342 965 150
# 630 803 746 422 111
# 537 699 497 121 956
# 805 732 524  37 331
#
# Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.
#

# Algorithmic approach thoughts: Recursive, dynamic programming most likely will be a good fit.

# (row, col) -> answer
cache ={}


def read_input(file):
    matrix = []
    for line in file:
        matrix.append([int(entry) for entry in line.strip().split(",")])
    width = len(matrix[0])
    for row in matrix:
        assert len(row) == width

    return matrix

def min_path_sum(matrix, row, col):
    if (row, col) in cache:
        return cache[(row, col)]
    max_row = len(matrix) - 1
    max_col = len(matrix[0]) - 1
    answer = None
    if row == max_row and col == max_col:
        answer = matrix[row][col]
    elif col == max_col:
        answer = matrix[row][col] + min_path_sum(matrix, row+1, col)
    elif row == max_row:
        answer = matrix[row][col] + min_path_sum(matrix, row, col+1)
    else:
        answer = matrix[row][col] + min(min_path_sum(matrix, row, col+1), min_path_sum(matrix, row+1, col))
    cache[(row, col)] = answer
    return answer

def solve(filename):
    with open(filename) as in_file:
        mat = read_input(in_file)
    return min_path_sum(mat, 0, 0)

if __name__ == '__main__':
    print(solve("matrix.txt"))
