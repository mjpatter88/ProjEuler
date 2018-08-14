from solver import fact, fact_sum

def test_fact_1():
    assert fact(1) == 1

def test_fact_2():
    assert fact(2) == 2

def test_fact_3():
    assert fact(3) == 6

def test_fact_10():
    assert fact(10) == 3628800

def test_fact_sum_1():
    assert fact_sum(1) == 1

def test_fact_sum_11():
    assert fact_sum(11) == 2

def test_fact_sum_13():
    assert fact_sum(13) == 7
