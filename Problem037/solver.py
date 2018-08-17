# 
# 
# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
# 
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# 
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
# 

def primes(limit):
    candidates = [True] * limit
    candidates[0] = False
    candidates[1] = False

    for i, is_prime in enumerate(candidates):
        if is_prime:
            for n in range(i, limit, i):
                candidates[n] = False
            yield i

def is_truncatable(num, primes):
    if num < 10:
        return False

    # From left
    s = str(num)
    s = s[1:]
    while s:
        if int(s) not in primes:
            return False
        s = s[1:]

    # From right
    s = str(num)
    s = s[:-1]
    while s:
        if int(s) not in primes:
            return False
        s = s[:-1]

    return True

def solve():
    sum = 0
    ps = set(prime for prime in primes(10000000))
    # ps = set(prime for prime in primes(100))
    for prime in ps:
        if is_truncatable(prime, ps):
            sum += prime
            print(prime)

    return sum


if __name__ == '__main__':
    print(solve())
