import time
from collections import deque

t = time.process_time()

def get_rotations(num):
    circs = []
    strnum = deque(str(num))
    for i in range(len(strnum)):
        circs.append(int(''.join(strnum)))
        strnum.rotate()
    return circs

def get_primes(limit):
    cur_prime = 2
    primes = {cur_prime}
    nums = [2] + list(range(3, limit, 2))

    while nums[-1] > cur_prime ** 2:
        nums = [num for num in nums if num % cur_prime]
        cur_prime = nums[0]
        primes.add(nums[0])
    return primes | set(nums)

limit = 1000000

primes = get_primes(limit)
circ_primes = [prime for prime in primes if all(num in primes for num in get_rotations(prime))]
print("{} primes".format(len(primes)))
print("{} circular primes".format(len(circ_primes)))

print("Elapsed time: {:.5} seconds".format(time.process_time() - t))
