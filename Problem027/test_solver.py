from solver import get_num_consec_primes, primes

def test_get_num_consec_primes_41():
    assert get_num_consec_primes(1, 41) == 40

def test_get_num_consec_primes_126479():
    assert get_num_consec_primes(-79, 1601) == 80
