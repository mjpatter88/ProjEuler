from string import ascii_lowercase
from itertools import permutations

with open('p059_cipher.txt') as in_file:
    data = in_file.read()
    chars = [int(char) for char in data.split(',')]

total = len(chars)

best_chars = ['', '', '']
best_num_good = [0, 0, 0]

for letter in ascii_lowercase:
    ascii_code = ord(letter)
    cur_num_good = [0,0,0]

    for index, char in enumerate(chars):
        new_char = char ^ ascii_code
        if chr(new_char) in ascii_lowercase:
            cur_num_good[index %3] += 1
    
    for x in range(0, 3):
        if cur_num_good[x] > best_num_good[x]:
            best_num_good[x] = cur_num_good[x]
            best_chars[x] = ascii_code

print(best_chars)
print(best_num_good)


total = 0
new_chars = []
for index, char in enumerate(chars):
    ascii_code = best_chars[index % 3]
    new_char = char ^ ascii_code
    total += new_char
    new_chars.append(chr(new_char))

print("".join(new_chars))
print(f"Total: {total}")