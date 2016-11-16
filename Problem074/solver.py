import time
import math
from collections import Counter

t = time.process_time()

def get_digit_factorial_sum(num):
    digits = [int(digit) for digit in str(num)]
    return sum(math.factorial(digit) for digit in digits)

cached_results = {}

def get_factorial_chain_length(num, chain=None):
    # Dynamic Programming
    if num in cached_results:
        length = len(chain) + cached_results[num]
        cached_results[chain[0]] = length
        return length

    if chain is None:
        chain = []
    chain.append(num)

    n = get_digit_factorial_sum(num)
    if n in chain:
        cached_results[chain[0]] = len(chain)
        return len(chain)
    else:
        return get_factorial_chain_length(n, chain)

counts = Counter(get_factorial_chain_length(num) for num in range(1000000))

assert cached_results[145] == 1
assert cached_results[69] == 5

print(counts[60])

print("Elapsed time: {:.5} seconds".format(time.process_time() - t))
