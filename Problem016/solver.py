import math
import string

num = math.pow(2, 1000)
# We need to use a format string since it defaults to scientific notation
s = "{:f}".format(num)
print(s)

answer = sum(int(c) for c in s if c in string.digits)
print(answer)
