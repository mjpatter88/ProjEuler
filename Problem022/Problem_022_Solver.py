#!/usr/bin/python3

'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing 
over five-thousand first names, begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, multiply this value 
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, 
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

Answer: 871198282
'''

def main():
    print("Running")

    # Read all the names into an array
    with open('p022_names.txt') as inp:
        names = inp.readline().split('","')
    # The split strips out all the quotes but the first and last.
    # The next two lines do that.
    names[0] = names[0][1:]
    names[len(names)-1] = names[len(names)-1][:-1]

    print(len(names))
    
    # Sort the array alphabetically
    names.sort()

    # Get the values
    total = 0
    for index, name in enumerate(names):
        total += (index + 1) * get_value_of_name(name)
        if(name == "COLIN"):
            print("COLIN: " + str((index+1)*get_value_of_name(name)))

    print("TOTAL: " + str(total))

    return

def get_value_of_name(name):
    value = 0
    for letter in name:
        value += ord(letter) - 64 # We know all the letters are caps. ord(A) - 64 = 1
    return value



if __name__ == '__main__':
    main()
