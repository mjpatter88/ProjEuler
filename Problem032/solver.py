# 
# 
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# 
# The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# 
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
# 

pandigital_chars = set(['1','2','3','4','5','6','7','8','9'])

def solve():
    products = set()
    for a in range(1, 100000):
        num_digits = 9 - len(str(a))
        for b in range(1, 10 ** num_digits):
            c = a * b
            s = str(a) + str(b) + str(c)
            if len(s) > 9:
                break
            if set(s) == pandigital_chars:
                products.add(c)
                print(f"{a} * {b} = {c}")
    return sum(products)


if __name__ == '__main__':
    print(solve())
