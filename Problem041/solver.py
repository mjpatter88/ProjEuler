

# Naively, the limit should be 987,654,321 but we can narrow the space using
# the trick that if the sum of digits is divisible by 3, then the number is
# divisible by three, and thus not a prime.
# sum(9,8,7,6,5,4,3,2,1) = 45
# sum(8,7,6,5,4,3,2,1) = 36
# sum(7,6,5,4,3,2,1) = 28
# There is a chance it could be smaller than this, but we can try that if we
# don't find one with digits 1 -> 7
LIMIT = 7_654_321
primes = []
sieve = [True] * LIMIT
sieve[0] = False
sieve[1] = False

for index, val in enumerate(sieve):
    if val:
        primes.append(index)
        # I think we can start at index * index since 1 -> index * (index-1)
        # should already be covered...
        product = index * index
        while product < LIMIT:
            sieve[product] = False
            product += index

print(len(primes))

def is_pandigital(num):
    return set(str(num)) == {"1", "2", "3", "4", "5", "6", "7"}

# Traverse backwards until we find a pandigital value
for val in reversed(primes):
    if is_pandigital(val):
        print(val)
        break
