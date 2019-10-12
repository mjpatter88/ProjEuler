from solver import min_path_sum, min_path_total

mat = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331]
]

mat2 = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [1, 1, 1, 1, 2]
]

mat3 = [
    [131, 673, 234, 1, 18],
    [201, 96, 342, 1, 150],
    [630, 803, 746, 1, 111],
    [537, 699, 497, 1, 956],
    [1, 1, 1, 1, 100]
]


def test_min_path_sum__end():
    assert min_path_sum(mat, 4, 4, None) == 331

def test_min_path_sum__end_2():
    assert min_path_sum(mat, 2, 4, None) == 111

def test_min_path_sum__top():
    assert min_path_sum(mat, 0, 3, None) == 103 + 18

def test_min_path_sum__full():
    assert min_path_sum(mat, 1, 0, None) == 201 + 96 + 342 + 234 + 103 + 18

def test_min_path_total__full():
    assert min_path_total(mat) == 201 + 96 + 342 + 234 + 103 + 18

def test_min_path_total__bottom():
    assert min_path_total(mat2) == 6

def test_min_path_total__l():
    assert min_path_total(mat3) == 8 + 18