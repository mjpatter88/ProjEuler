# 
# 
# A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
# 
# Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
# 
import math
LIMIT = 100

def solve(limit):
    max_sum = 0
    for a in range(1, limit):
        for b in range(1, limit):
            s = a ** b
            digit_sum = sum(int(digit) for digit in str(int(s)))
            max_sum = max(digit_sum, max_sum)

    return max_sum

if __name__ == '__main__':
    print(solve(LIMIT))
