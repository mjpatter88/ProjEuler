# 
# 
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# 
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# 
# (Please note that the palindromic number, in either base, may not include leading zeros.)
# 
LIMIT = 1000000

def is_pal_dec(num):
    s = str(num)
    rev = "".join(reversed(s))
    return s == rev

def is_pal_bin(num):
    s = str(bin(num))
    s = s[2:] # remove the leading "0b" from the binary representation
    rev = "".join(reversed(s))
    return s == rev

def is_pal(num):
    return is_pal_dec(num) and is_pal_bin(num)

def solve(limit):
    total = 0
    for i in range(limit):
        if is_pal(i):
            total += i
    return total

if __name__ == '__main__':
    print(solve(LIMIT))
