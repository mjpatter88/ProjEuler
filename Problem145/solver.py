# I tried several approaches but they were all too slow.
# This runs in about 10-15 minutes.
LIMIT = 1000000000
# LIMIT = 10000000
# LIMIT = 1000


def check_odd(num):
    if num == 0:
        return True
    if num % 2 == 0:
        return False
    return check_odd(num // 10)


def reversible(num):
    if num % 10 == 0:
        return False
    s = num + int("".join(reversed(str(num))))
    return check_odd(s)


# You can only check odd numbers and then count double for each hit
# to account for the corresponding even number you would hit
# Ex: 102 and 201 (count 201 twice because we are skipping 102)
def solve(limit):
    answer = 0
    x = 11
    while x <= limit:
        if reversible(x):
            answer += 2
        x += 2

    return answer


if __name__ == "__main__":
    import time
    start_time = time.time()
    print(solve(LIMIT))
    print(f"----- {time.time() - start_time} seconds -----")
