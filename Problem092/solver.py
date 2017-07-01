
def sum_of_digit_squares(number):
    return sum(int(digit) ** 2 for digit in str(number))


# Square digit number chains always arrive at either 1 or 89.
# These sets can be used as a cache, since chains at x always resolve consistently.
resolve_to_1 = {1}
resolve_to_89 = {89}


# sum_of_digit_squares(9999999) = 567, so every number resolves to <= 567 in single step
# Store nums that resolve to 89 for all nums < 567.
# Then loop through 567 -> 10,000,000. Find first SoSD, if in list, add to count.

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

count = len(resolve_to_89)

for x in range(568, 10000000):
    num = sum_of_digit_squares(x)
    if num in resolve_to_89:
        count += 1


print(f"Number of starting numbers below ten million that arrive at 89: {count}")
