from solver import solve


def test_solve_100():
    assert 41 == solve(100)

def test_solve_1000():
    assert 953 == solve(1000)
