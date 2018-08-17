'''
Project Euler Problem 31:


In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?

Answer:

'''


'''
Thoughts:
The obvious solution would be brute force, trying every combination.

A much better approach would utilize dynamic programming and recursion.
After writing out a few test cases, it seems that I could achieve the
same result by working backwards. Start by determining how many ways to
make 1p, then 2p, then 3p, etc. Each time, take the total we already
found for 1p less, then add 1 for each coin that evenly divides the value.

That's not actually quite right either... I'll need to work on this one some more.
I think DP is the way to go though.

The problem is that order isn't important: 12 is the same as 21 and only count as 1 way total.

To get around this, we need to go coin by coin.
The question is "How many ways are there to make the given amount with the max coin being y."
This solves the ordering problem.

Examples:
    1p - 1
    2p - 11 | 2
    3p - 111 | 21
    4p - 1111 | 211 | 22
    5p - 11111 | 2111 | 221 | 5
    6p - 111111 | 21111 | 2211 | 222 | 51
    7p - 1111111 | 211111 | 22111 | 2221 | 511 | 52
    8p - 11111111 | 2111111 | 221111 | 22211 | 2222 | 5111 | 521

'''
from functools import lru_cache

AMOUNTS = [1, 2, 5, 10, 20, 50, 100, 200]

@lru_cache()
def ways(amount, max_coin_index):
    if amount == 0:
        return 1
    if max_coin_index == 0:
        return 1

    result = ways(amount, max_coin_index-1)
    amount_with_max_coin = AMOUNTS[max_coin_index]
    while amount_with_max_coin <= amount:
        result += ways(amount - amount_with_max_coin, max_coin_index-1)
        amount_with_max_coin += AMOUNTS[max_coin_index]
    return result


def solve(amount):
    return ways(amount, 7)


if __name__ == '__main__':
    print(solve(200))
