# 
# 
# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
# 
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# 
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
# 
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
# 
# 
import string

def gen_vals():
    return {letter: val+1 for val, letter in enumerate(string.ascii_lowercase)}

def gen_tris():
    results = []
    for i in range(100):
        results.append(int(i * (i+1) / 2))
    return set(results)

def get_string():
    return "".join(str(i) for i in range(1, 200000))

vals = gen_vals()

def get_val(word):
    return sum(vals[letter.lower()] for letter in word)

def solve(filename):
    tris = gen_tris()

    with open(filename) as in_file:
        words = in_file.read()
        words = words.strip().split(",")
        words = [word.strip('"') for word in words]
    print(len(words))

    count = 0
    for word in words:
        if get_val(word) in tris:
            count += 1

    return count


if __name__ == '__main__':
    print(solve("words.txt"))
