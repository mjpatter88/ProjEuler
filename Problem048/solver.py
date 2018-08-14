# 
# 
# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
# 
# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
# 
def solve(limit):
    total = 0
    for i in range(1, limit + 1):
        total += i ** i
    return str(total)[-10:]

if __name__ == '__main__':
    print(solve(1000))
