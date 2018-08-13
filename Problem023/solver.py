# 
# 
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# 
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
# 
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
# However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
# 
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
# 

import math
from itertools import combinations_with_replacement

LIMIT = 28123

def sums_of_combinations(numbers):
    return set([a+b for a,b in combinations_with_replacement(numbers, 2)])

def proper_divisors(num):
    proper_divisors = [1]
    # Need to add one to the upper bound for perfect squares.
    # Eg sqrt(9) = 3, which would exclude 3 but we want it included.
    for i in range(2, int(math.floor(math.sqrt(num))) + 1):
        if num % i == 0:
            proper_divisors.append(i)
            proper_divisors.append(int(num/i))
    # Need to exclude the number itself. Otherwise 2 would identify as it's own proper divisor
    return set(proper_divisors) - {num}

def abundant(upper_range):
    results = []
    for i in range(1, upper_range + 1):
        if sum(proper_divisors(i)) > i:
            results.append(i)
    return results

def solve(upper_limit):
    all_nums = set(range(upper_limit + 1))

    # Find all abundant numbers up to 28123
    abund_nums = abundant(upper_limit)
    print(f"Found {len(abund_nums)} abundant numbers")

    # Generate all the sums that can be made when combining two abundant numbers
    sums = sums_of_combinations(abund_nums)

    # Subtract that set from the set of all numbers 0 -> 28123
    numbers = all_nums - sums
    print(f"{len(numbers)} numbers remaining")
    # Sum up that set
    return sum(numbers)

if __name__ == '__main__':
    print(solve(LIMIT))
