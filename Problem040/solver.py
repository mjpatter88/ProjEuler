# 
# 
# An irrational decimal fraction is created by concatenating the positive integers:
# 
# 0.123456789101112131415161718192021...
# 
# It can be seen that the 12th digit of the fractional part is 1.
# 
# If dn represents the nth digit of the fractional part, find the value of the following expression.
# 
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
# 
#  Thoughts: Probably a clever way to do this, but it seems like brute force will be fast enough...
# 
# 


# trial and error to find a number that provides roughly 1 mil digits
def get_string():
    return "".join(str(i) for i in range(1, 200000))

def solve():
    s = get_string()
    return int(s[0]) * int(s[9]) * int(s[99]) * int(s[999]) * int(s[9999]) * int(s[99999]) * int(s[999999])


if __name__ == '__main__':
    print(solve())
