from solver import count_non_bouncy

def test_count_non_bouncy__100_99():
    assert count_non_bouncy(100) == 99

def test_count_non_bouncy__1000_475():
    assert count_non_bouncy(1000) == 474

def test_count_non_bouncy__1000000_12951():
    assert count_non_bouncy(1000000) == 12951

def test_count_non_bouncy__10_to_the_10_277032():
    assert count_non_bouncy(10 ** 10) == 277032
