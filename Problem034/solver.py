# 
# 
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# 
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# 
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
# 
facts = {}

def fact(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

def fact_sum(num):
    total = 0
    num_string = str(num)
    for digit in num_string:
        total += facts[int(digit)]
    return total

def solve():
    # calculate all the needed factorials (0-9) up front so you don't need to repeat the calculation
    for i in range(10):
        facts[i] = fact(i)

    total = 0
    i = 3
    while i < 1000000:
        if fact_sum(i) == i:
            total += i
            print(f"{i} - {total}")
        i += 1

if __name__ == '__main__':
    solve()
