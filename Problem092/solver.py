def sum_of_digit_squares(number):
    return sum(int(digit) ** 2 for digit in str(number))


# Square digit number chains always arrive at either 1 or 89.
# These sets can be used as a cache, since chains at x always resolve consistently.
resolve_to_1 = {1}
resolve_to_89 = {89}


# sum_of_digit_squares(9999999) = 567, so every number resolves to <= 567 in a single step
# precalculate nums that resolve to 89 for all nums < 567.
# this way the set of 'resolve to 89' doesn't have to always be updated

for num in range(1, 568):
    chain = [num]

    while True:
        if num in resolve_to_1:
            resolve_to_1.update(chain)
            break
        elif num in resolve_to_89:
            resolve_to_89.update(chain)
            break
        else:
            num = sum_of_digit_squares(num)
            chain.append(num)

count = 0

# loop 0 - 99,999. We need the 0 for 1,000,000, 2,000,000, etc.
# for each number, add SoS for each digit in the millionths place
# calculate intersection of all ten of these values
for x in range(0, 1000000):

    num = sum_of_digit_squares(x)
    nums = {num + inc for inc in (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)}
    count += len(nums.intersection(resolve_to_1))

print(f"Number of starting numbers below ten million that arrive at 89: {9999999 - count}")
