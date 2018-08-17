from solver import ways

def test_ways_00__returns_1():
    assert ways(0, 0) == 1

def test_ways_10__returns_1():
    assert ways(1, 0) == 1

def test_ways_90__returns_1():
    assert ways(9, 0) == 1

def test_ways_31__returns_2():
    assert ways(3, 1) == 2

def test_ways_41__returns_3():
    assert ways(4, 1) == 3

def test_ways_51__returns_3():
    assert ways(5, 1) == 3

def test_ways_52__returns_4():
    assert ways(5, 2) == 4

def test_ways_82__returns_7():
    assert ways(8, 2) == 7
