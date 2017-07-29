# Naive solution presented below seems fast enough
# With no output, takes about 4 seconds on ubuntu VM
# With output, 15 seconds


def is_bouncy(num):
    if num < 100:
        return False

    digits = str(num)
    increasing = all(digits[x+1] >= digits[x] for x in range(len(digits) - 1))
    decreasing = all(digits[x+1] <= digits[x] for x in range(len(digits) - 1))

    return not increasing and not decreasing

TARGET_PROPORTION = .99

total_bouncy = 0
bouncy_proportion = 0
x = 1
while bouncy_proportion != TARGET_PROPORTION:
    bouncy = 1 if is_bouncy(x) else 0
    total_bouncy += bouncy
    bouncy_proportion = total_bouncy / x
    print(f"\r{x}: {bouncy_proportion * 100 : .2f}% bouncy", end="")
    x += 1

# print(x-1)
print()
