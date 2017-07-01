
def sum_of_digit_squares(number):
    return sum(int(digit) ** 2 for digit in str(number))


# Square digit number chains always arrive at either 1 or 89.
# This dictionary is a mapping from start to either 1 or 89
# It can be used as a cache, since chains at x always resolve consistently.
resolve_to_1 = {1}
resolve_to_89 = {89}
nums = {x for x in range(1, 10000000)}

while nums:
    chain = []
    num = nums.pop()
    chain.append(num)

    while True:
        if num in resolve_to_1:
            resolve_to_1.update(chain)
            nums.difference_update(chain)
            break
        elif num in resolve_to_89:
            resolve_to_89.update(chain)
            nums.difference_update(chain)
            break
        else:
            num = sum_of_digit_squares(num)
            chain.append(num)


count = len(resolve_to_89)
print(f"Number of starting numbers below ten million that arrive at 89: {count}")
