I'd llke to solve this problem two ways.
First I'll write a recursive brute force method.
Then I'll write a dynamic programming method.
I'll compare the performance, and then try the dp method on problem 67.

This structure is similar to a binary tree, but slightly different since adjacent nodes share one child.
I think this technically makes it not a "tree" but I'm calling it that for now.
I'll first have to write some data structures and some routines to populate them from a text file of numbers.
Node class
Tree class
Main solver program.

I think I'll try this in C++. It would be easier for me in Java, C, or Python, but this will provide a good
challenge and force me to practice C++ data structures, pointers, etc.


I think the input file should basically look like:

75
95 64
17 47 82
...

(This is also the format used in problem 67. Also in both problems all values are 2 digit numbers.)
I can maybe pull all the text out of the website source? Will have to check on this.
