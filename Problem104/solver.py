import math
import string

# define some constants
# Note: Using these constants actually broke my solution. I believe it was due to rounding, but my calculation
# of the first nine digits was off by one so it didn't work :/
LOG_PHI = 0.20898764024997573
LOG_SQRT_5 = 0.3494850021680094

# use this to grab the last 9 digits
tail_cut = 1000000000

digits = set(string.digits)
digits.discard('0')

def is_pandigital(numbers):
    return set(numbers) == digits


fib = 1
a = 0
b = 1
for index in range(1, 500000):

    # findind the least significant digits is easy now since we are only calcing them and not whole numbers

    # finding the first digits by calcing the whole number and slicing is way too slow ( > 5 mins)
    # instead, we calc the first nine digits directly using phi, log, etc.
    # references:
    # https://en.wikipedia.org/wiki/Fibonacci_number
    # http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibFormula.html

    least_nine = str(fib)
    if is_pandigital(least_nine):
        # val = index * LOG_PHI - LOG_SQRT_5 # See references above
        val = index * 0.20898764024997873 - 0.3494850021680094 # See references above

        # since this is a logarithm, we only care about the decimals here
        # also we need this so the math.pow call that follows doesn't overflow into a giant number
        # this whole optimization is to throw away digits we don't care about
        val = val - int(val)

        # we add 8 to get 9 digits (we get one for free due to how log works)
        first_digits = int(math.pow(10, val + 8))
        if is_pandigital(str(first_digits)):
            print(F"Answer: {index}")
            break

    # This will only store/return the 9 least sig digits
    # Which is a huge performance boost since we aren't dealing with thousands of digits
    fib = (a + b) % tail_cut
    a, b = b, fib

# NOTE: works in about 0.5 seconds on vm on desktop
