# The key insight for this problem is that you can get the number of digits in
# a ^ b by doing b * log(a, 10). This is a must faster operation than actually
# calculating the value of the exponent.
import math
import operator

lines_to_num_digits = {}

with open("base_exp.txt") as in_file:
    lines = [line.strip() for line in in_file.readlines()]

for index, line in enumerate(lines):
    base, exp = line.split(',')
    num_digits = int(exp) * math.log(int(base), 10)
    lines_to_num_digits[index] = num_digits

max_index = max(lines_to_num_digits.items(), key=operator.itemgetter(1))[0]

# Add 1 to the answer to account for 0 indexing.
print(max_index+1)
