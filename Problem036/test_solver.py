from solver import is_pal_dec, is_pal_bin

def test_is_pal_dec_1():
    assert is_pal_dec(1) == True

def test_is_pal_dec_11():
    assert is_pal_dec(11) == True

def test_is_pal_dec_101():
    assert is_pal_dec(101) == True

def test_is_pal_dec_100():
    assert is_pal_dec(100) == False

def test_is_pal_dec_585():
    assert is_pal_dec(585) == True


def test_is_pal_bin_1():
    assert is_pal_bin(1) == True

def test_is_pal_bin_11():
    assert is_pal_bin(11) == False

def test_is_pal_bin_585():
    assert is_pal_bin(585) == True
