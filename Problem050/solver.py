# 
# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# 
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# 
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
# 
# Which prime, below one-million, can be written as the sum of the most consecutive primes?
# 

def gen_primes(limit):
    candidates = [True] * limit
    candidates[0] = False
    candidates[1] = False

    for i, is_prime in enumerate(candidates):
        if is_prime:
            for n in range(i, limit, i):
                candidates[n] = False
            yield i


def solve(limit):
    consec_prime_len = 0
    consec_prime_sum = 0
    primes = list(prime for prime in gen_primes(limit))
    prime_set = set(primes)
    max_prime = max(primes)
    cur_len = 0
    running = True
    while cur_len < len(primes):
        starting_index = 0
        starting_sum = sum(primes[starting_index:starting_index+cur_len])

        if cur_len % 100 == 0:
            print(cur_len)
            print(starting_sum)

        if starting_sum > 1000000:
            print("Done")
            break

        while starting_index <= (len(primes) - cur_len):
            new_sum = sum(primes[starting_index:starting_index+cur_len])
            if new_sum in prime_set:
                if cur_len > consec_prime_len:
                    consec_prime_len = cur_len
                    consec_prime_sum = new_sum
                    print(f"Length: {consec_prime_len}")
                    print(f"Sum: {consec_prime_sum}")
            starting_index += 1
        cur_len += 1

    print(f"Length: {consec_prime_len}")
    return consec_prime_sum

if __name__ == '__main__':
    print(solve(1000000))
