#include <iostream>

#include "Node.h"
#include "Tree.h"


int main(int argc, char* argv[])
{
    Node test;
    test.setTest(5);
    std::cout << test.getTest() << std::endl;
    test.setTest(7);
    std::cout << test.getTest() << std::endl;

    Tree test2;
    test2.setTest(5);
    std::cout << test2.getTest() << std::endl;
    test2.setTest(7);
    std::cout << test2.getTest() << std::endl;
}
