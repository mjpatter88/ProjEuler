
def sum_of_digit_squares(number):
    return sum(int(digit) ** 2 for digit in str(number))


# Square digit number chains always arrive at either 1 or 89.
# This dictionary is a mapping from start to either 1 or 89
# It can be used as a cache, since chains at x always resolve consistently.
results = {1:1, 89:89}
nums = {x for x in range(1, 10000000)}

while nums:
    chain = []
    num = nums.pop()
    chain.append(num)

    while num != 1 and num != 89:
        if num in results:
            num = results[num]
        else:
            num = sum_of_digit_squares(num)
            chain.append(num)

    for start in chain:
        results[start] = num
        nums.discard(start)


count = sum(1 for res in results.values() if res == 89)
print(f"Number of starting numbers below ten million that arrive at 89: {count}")
