from solver import get_factorials, comb

def test_factorial_1():
    assert get_factorials(100)[1] == 1

def test_factorial_2():
    assert get_factorials(100)[2] == 2

def test_factorial_3():
    assert get_factorials(100)[3] == 6

def test_factorial_4():
    assert get_factorials(100)[4] == 24

def test_comb_5_3():
    assert comb(5, 3) == 10
