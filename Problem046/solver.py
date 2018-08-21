# 
# 
# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
# 
# 9 = 7 + 2×12
# 15 = 7 + 2×22
# 21 = 3 + 2×32
# 25 = 7 + 2×32
# 27 = 19 + 2×22
# 33 = 31 + 2×12
# 
# It turns out that the conjecture was false.
# 
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
# 
import math

def gen_primes(limit):
    candidates = [True] * limit
    candidates[0] = False
    candidates[1] = False

    for i, is_prime in enumerate(candidates):
        if is_prime:
            for n in range(i, limit, i):
                candidates[n] = False
            yield i



def gen_odd_composites(limit):
    candidates = [True] * limit
    candidates[0] = False
    candidates[1] = False

    for i, is_prime in enumerate(candidates):
        if is_prime:
            for n in range(i, limit, i):
                candidates[n] = False
        elif i > 1 and i % 2 != 0:
            yield i

LIMIT = 10000
primes = list(prime for prime in gen_primes(LIMIT))
odd_comp_num = list(np for np in gen_odd_composites(LIMIT))

def solve():
    answer = 0
    for oc in odd_comp_num:
        found = False
        for i in range(1, int(math.sqrt(oc))):
            if (oc - 2 * (i ** 2)) in primes:
                found = True
                break
        if not found:
            answer = oc
            break
    return answer

if __name__ == '__main__':
    print(f"\n{solve()}")
