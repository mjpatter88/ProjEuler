# NOTE: This problem is a significantly more challenging version of Problem 81.
#
# In the 5 by 5 matrix below, the minimal path sum from the top left to the
# bottom right, by moving left, right, up, and down, is indicated in bold
# red and is equal to 2297.
#
# 131 673 234 103 18
# 201  96 342 965 150
# 630 803 746 422 111
# 537 699 497 121 956
# 805 732 524  37 331
#
# 131 -> 201 -> 96 -> 342 -> 234 -> 103 -> 18 -> 150 -> 111 -> 422 -> 121 -> 37 -> 331
#
# Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."),
# a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right
# by moving left, right, up, and down.
#
# Algorithmic approach thoughts: I don't think I can use recursion/dynamic programmming.
# I think Djikstra's should work for this though.

import math


class Graph:
    def __init__(self):
        self.nodes = []
        self.head = None
        self.end = None

class Node:
    def __init__(self, value, start=False, end=False):
        self.value = value
        self.start = start
        self.end = False
        self.neighbors = []
        self.visited = False
        self.previous = None
        # For Dijkstra's, start all non-head nodes at infinity.
        # Normally start source at 0, but here the value of the node
        # is the cost.
        self.distance = math.inf if not start else value
    
    def __str__(self):
        return str(self.value)

# map x,y to Node
already_built = {}

def build_graph(matrix):
    g = Graph()
    g.head = build_node(matrix, 0, 0, g)
    return g

def build_node(matrix, row, col, graph):
    if (row, col) in already_built:
        return already_built[(row, col)]
    end_row = len(matrix) - 1
    end_col = len(matrix[0]) - 1
    start = row == 0 and col == 0
    end = row == end_row and col == end_col

    new_node = Node(matrix[row][col], start=start, end=end)
    already_built[(row, col)] = new_node
    graph.nodes.append(new_node)
    if end:
        graph.end = new_node

    neighbors = []
    if row > 0:
        neighbors.append(build_node(matrix, row-1, col, graph))
    if row < end_row:
        neighbors.append(build_node(matrix, row+1, col, graph))
    if col > 0:
        neighbors.append(build_node(matrix, row, col-1, graph))
    if col < end_col:
        neighbors.append(build_node(matrix, row, col+1, graph))
    new_node.neighbors.extend(neighbors)
    return new_node

def read_input(file):
    matrix = []
    for line in file:
        matrix.append([int(entry) for entry in line.strip().split(",")])
    width = len(matrix[0])
    for row in matrix:
        assert len(row) == width

    return matrix

def pop_shortest(verts):
    # This could be faster (using a min_heap possibly)?
    m = min(verts, key=lambda vert: vert.distance)
    verts.remove(m)
    return m

def min_path_sum(graph):
    # Huge speed up by only tracking nodes as we encounter them
    # rather than starting with all nodes as unvisited.
    unvisited_verts = [graph.head]

    while unvisited_verts:
        node = pop_shortest(unvisited_verts)
        node.visited = True

        for n in node.neighbors:
            new_dist = node.distance + n.value
            if new_dist < n.distance:
                n.distance = new_dist
                n.previous = node
                # This could add a duplicate node to the list.
                # It doesn't cause a problem here, but it could be avoided
                # if needed.
                unvisited_verts.append(n)
    
    path_values = []
    n = graph.end
    while n:
        path_values.append(str(n.value))
        n = n.previous
    print(" -> ".join(reversed(path_values)))

    return graph.end.distance

def solve_matrix(matrix):
    graph = build_graph(matrix)
    print(f"Graph built with {len(graph.nodes)} nodex.")
    return min_path_sum(graph)

def solve(filename):
    with open(filename) as in_file:
        mat = read_input(in_file)
    return solve_matrix(mat)

if __name__ == '__main__':
    # The recursion used to build the graph exceeds the default limit.
    import sys
    sys.setrecursionlimit(7000)
    print(solve("matrix.txt"))
