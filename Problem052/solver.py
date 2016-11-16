import time

t = time.process_time()

# Lots of speedups possible, multipls of 3 and 9, etc.
# http://www.wolframalpha.com/input/?x=0&y=0&i=cyclic+number
# Current form is pretty simply though.
def gen_nums(factor):
    num = 1
    while True:
        yield num

        num += 1

        # We can skip numbers if we know 6 * n will result in an etra digit
        y = float(str(num)[0] + '.' + str(num)[1:])
        if y > 10 / factor:
            num = 10 ** len(str(num))

def factors_have_same_digits(factors, i):
    return all(sorted(str(i)) == sorted(str(i*factor)) for factor in factors)

factors = [1, 2, 3, 4, 5, 6]
for i in gen_nums(factors[-1]):
    if factors_have_same_digits(factors[1:], i):
        print(', '.join(map(str, (i * factor for factor in factors))))
        break

print("Elapsed time: {:.5} seconds".format(time.process_time() - t))
