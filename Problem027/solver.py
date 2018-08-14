# Euler discovered the remarkable quadratic formula:
# 
# n2+n+41
# 
# It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39
# . However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41
# 
# is clearly divisible by 41.
# 
# The incredible formula n2−79n+1601
# was discovered, which produces 80 primes for the consecutive values 0≤n≤79
# 
# . The product of the coefficients, −79 and 1601, is −126479.
# 
# Considering quadratics of the form:
# 
#     n2+an+b
# 
# , where |a|<1000 and |b|≤1000
# 
# where |n|
# is the modulus/absolute value of n
# e.g. |11|=11 and |−4|=4
# 
# Find the product of the coefficients, a
# and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
# 

A_MIN = -1000
B_MIN = -1001
A_MAX = 1000
B_MAX = 1001

PRIME_LIMIT = 1000000

def get_primes(limit):
    primes = []
    candidates = [True] * limit
    candidates[0] = False
    candidates[1] = False

    for i, is_prime in enumerate(candidates):
        if is_prime:
            primes.append(i)
            for n in range(i, limit, i):
                candidates[n] = False
    return set(primes)

primes = get_primes(PRIME_LIMIT)

def is_prime(num):
    assert num < PRIME_LIMIT
    return num in primes

def quadratic(a, b, n):
    return (n*n) + (a * n) + b

def get_num_consec_primes(a, b):
    n = 0
    while is_prime(quadratic(a, b, n)):
        n += 1
    return n

def solve():
    a_max = 0
    b_max = 0
    max_primes = 0

    for a in range(A_MIN, A_MAX):
        for b in range(B_MIN, B_MAX):
            num_primes = get_num_consec_primes(a, b)
            if num_primes > max_primes:
                max_primes = num_primes
                a_max = a
                b_max = b

    return a_max * b_max

if __name__ == '__main__':
    print(solve())
