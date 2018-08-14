from solver import min_path_sum

mat = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331]
]

def test_min_path_sum__end():
    assert min_path_sum(mat, 4, 4) == 331

def test_min_path_sum__right_edge():
    assert min_path_sum(mat, 3, 4) == 956 + 331

def test_min_path_sum__right_edge_full():
    assert min_path_sum(mat, 0, 4) == 18 + 150 + 111 + 956 + 331

def test_min_path_sum__bottom_edge():
    assert min_path_sum(mat, 4, 3) == 37 + 331

def test_min_path_sum__bottom_edge_full():
    assert min_path_sum(mat, 4, 0) == 805 + 732 + 524 + 37 + 331

def test_min_path_sum__middle():
    assert min_path_sum(mat, 3, 3) == 121 + 37 + 331

def test_min_path_sum__full():
    assert min_path_sum(mat, 0, 0) == 131 + 201 + 96 + 342 + 746 + 422 + 121 + 37 + 331
