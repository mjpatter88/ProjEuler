from solver import solve_matrix

mat = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331]
]


def test_min_path_total__l():
    assert solve_matrix(mat) == 2297