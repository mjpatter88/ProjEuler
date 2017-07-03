import math

def get_proper_divisors(num):
    # 1 is always a proper divisor, but num itself isn't
    d = [1]
    for x in range(2, int(math.sqrt(num))):
        if num % x == 0:
            d.append(x)
            d.append(num // x)
    return d

def sum_of_proper_divisors(num):
    return sum(get_proper_divisors(num))

amicables = set()

for a in range(1, 10000):
    b = sum_of_proper_divisors(a)
    if a == sum_of_proper_divisors(b):
        # Don't add pair if it's already been added or if a == b
        if (b, a) not in amicables and b != a:
            amicables.add((a, b))

print(f"amicables < 10,000: {amicables}")
answer = sum(first + second for first, second in amicables)
print(f"sum: {answer}")

