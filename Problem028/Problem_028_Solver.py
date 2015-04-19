#!/usr/bin/python3

'''
Project Euler Problem 28:

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

Answer: 66917100
    
'''


''' Thoughts:

1x1  1
3x3  3  5  7  9   +2
5x5  13 17 21 25  +4
7x7  31 37 43 49  +6
9x9  57 65 73 81  +8

Nested for loops, increment the dimensions, keep a 'cur number' variable
and an 'incremental value' variable, keep a running sum.

May be a formula? Not sure...

'''
TEST_LIMIT = 5 # See if we can get the same value as the example
LIMIT = 1001 # From problem definition

def main():
    print("Solving Problem 28...")

    dimension = 3
    total_of_diagonals = 1
    increment_value = 2
    cur_value = 1

    while dimension <= LIMIT:
        for x in range(4):
            cur_value += increment_value
            total_of_diagonals += cur_value
        increment_value += 2
        dimension += 2

    print("Total: " + str(total_of_diagonals))


if __name__ == '__main__':
    main()

