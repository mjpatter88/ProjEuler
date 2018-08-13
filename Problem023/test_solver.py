from solver import abundant, solve, proper_divisors, sums_of_combinations

def test_sum_of_combinations():
    numbers = [1,2,3]
    assert {2, 3, 4, 5, 6} == sums_of_combinations(numbers)

def test_proper_divisors():
    assert set([1]) == proper_divisors(2)

def test_proper_divisors_12():
    assert set([1, 2, 3, 4, 6]) == proper_divisors(12)

def test_proper_divisors_9():
    assert set([1, 3]) == set(proper_divisors(9))

def test_abundant():
    assert [12] == abundant(12)

def test_abundant_30():
    assert [12, 18, 20, 24, 30, 36, 40, 42, 48, 54, 56, 60, 66, 70, 72, 78, 80, 84, 88, 90, 96, 100, 102, 104, 108, 112, 114, 120] == abundant(120)

def test_solve():
    answer = sum(range(30)) + 31 + 33 - 24
    assert answer == solve(33)
