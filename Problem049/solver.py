# 
# 
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
# 
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
# 
# What 12-digit number do you form by concatenating the three terms in this sequence?
# 

from itertools import permutations
PRIME_LIMIT = 10000

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

def solve():
    primes = get_primes(PRIME_LIMIT)
    for i in range(1000, 10000):
        prime_perms = set()
        for perm in permutations(str(i)):
            p = int(''.join(perm))
            if p in primes:
                prime_perms.add(p)
        if len(prime_perms) >= 3:
            print(prime_perms)
    return

if __name__ == '__main__':
    print(solve())
