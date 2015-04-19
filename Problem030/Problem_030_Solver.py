#!/usr/bin/python3

'''
Project Euler Problem 30:

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

Answer: 443839

'''
# Not really sure what to use as an upper bound... I learned the following:
# 9^5 = 59049, so each digit can only contribute at most that amount to the sum
# 7*9^5 = 413343, which is only 6 digits, so it's impossible for a 7-digit
# number to ever sum up to itselt. It only gets worse as you go.
# So checking all 6 digit numbers is more than sufficient.
LIMIT = 1000000

def main():
    print("Solving Problem 30.")
    total = 0
    for x in range(2, LIMIT):
        if sumOfPowers(x) == x:
            print(x)
            total += x
    print("Sum: " + str(total))

    
# For a given number, compute the sum of the fifth powers of its digits
def sumOfPowers(num):
    total = 0
    for x in range(0, len(str(num))):
        digit = int(str(num)[x])
        total += digit ** 5
    return total

if __name__ == '__main__':
    main()
