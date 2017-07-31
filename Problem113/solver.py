from functools import lru_cache

inc_cache = {}

def count_non_bouncy(num):
    zero_to_remove = str(num)[1:] # Remove 0000.... as results require positive integers
    num = str(num - 1)

    incs = get_incs(0, num)
    decs = get_decs(0, num, True)

    unique_non_bouncy = set(incs + decs)
    unique_non_bouncy.remove(zero_to_remove)

    return len(unique_non_bouncy)

def get_incs(prev_digit, digits):
    cache_key = (prev_digit, digits)
    if cache_key in inc_cache:
        return inc_cache[cache_key]

    # If num is single digit, then return single numbers greater than or equal the prev_digit
    if len(digits) < 2:
        ret_val = list(map(str, range(prev_digit, (int(digits)+1))))
        inc_cache[cache_key] = ret_val
        return ret_val

    # Otherwise break up and use a recursive call
    first_digit = int(digits[0])
    remainder = digits[1:]

    nums = []
    
    for x in range(prev_digit, first_digit+1):
        remainders = get_incs(x, remainder)
        nums.extend(str(x) + r for r in remainders)

    inc_cache[cache_key] = nums
    return nums

# old method. It works, but is slow
#@lru_cache(maxsize=2048)
#def get_incs(prev_digit, digits):
#
#    # If num is single digit, then return single numbers greater than or equal the prev_digit
#    if len(digits) < 2:
#        ret_val = list(map(str, range(prev_digit, (int(digits)+1))))
#        return ret_val
#
#    # Otherwise break up and use a recursive call
#    first_digit = int(digits[0])
#    remainder = digits[1:]
#
#    nums = []
#    
#    for x in range(prev_digit, first_digit+1):
#        remainders = get_incs(x, remainder)
#        nums.extend(str(x) + r for r in remainders)
#
#    return nums

@lru_cache(maxsize=1024)
def get_decs(prev_digit, digits, all_prev_digits_zero):
    return []
    # If all prev digits are zero so far, any digit is an options, so start at 9
    if all_prev_digits_zero:
        prev_digit = 9
    # If num is single digit, then return single numbers less than or equal the prev_digit
    if len(digits) < 2:
        return list(map(str, reversed(range(0, (int(prev_digit)+1)))))

    # Otherwise break up and use a recursive call
    first_digit = int(digits[0])
    remainder = digits[1:]

    nums = []
    
    for cur_digit in reversed(range(0, prev_digit + 1)):
        new_all_prev_digits_zero = all_prev_digits_zero and (cur_digit == 0)
        remainders = get_decs(cur_digit, remainder, new_all_prev_digits_zero)
        nums.extend(str(cur_digit) + r for r in remainders)

    return nums

# TODO: I believe it works, now make it fast. DP? Cache intermediate results?
# @lru_cache?
num_range = 10 ** 17
# num_range = 1000

num = count_non_bouncy(num_range)

print(f"{num} non-bouncy numbers below {num_range}.")
# print(f"{num} non-bouncy numbers below a googol (10^100).")
