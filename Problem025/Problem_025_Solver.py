#!/usr/bin/python3
'''
Project Euler Problem 25:

What is the first term in the Fibonacci sequence to contain 1000 digits?

Answer: 4782

'''

numbers = [1, 1, 2, 3, 5] # Seed with a few starting values

def getNextFib():
    length = len(numbers)
    numbers.append(numbers[length-2] + numbers[length-1])
    return numbers[length]

def main():
    print("Solving Problem 25...")
    number = 0
    while len(str(number)) < 1000:
        number = getNextFib()

    print(number)
    print("Term: " + str(len(numbers)))

if __name__ == '__main__':
    main()
