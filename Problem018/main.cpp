/*
 * Answer: 1074
 */
#include <iostream>
#include <fstream>
#include <algorithm>

#define NUM_ROWS 15

void bruteSolve(int** arr);
void dynSolve(int **arr);
void printArr(int **arr);
int recSolve(int** arr, int row, int col);

int main(int argc, char* argv[])
{
    /*
     * For now we will be using jagged 2D arrays for lack of a better data structure.
     * I'll write a "slow" brute force method and a "fast" dynamic programming one.
     */

    //First we need an array of pointers
    int** arr = new int*[NUM_ROWS];
    for(int i=0; i<NUM_ROWS; i++)   //Create each inner array
    {
        arr[i] = new int[i+1];  //Each row has one more element than the previous
    }


    std::string fileName = "numbers.txt";
    std::ifstream inputFile(fileName.c_str());
    if(!inputFile.is_open())
    {
        std::cerr << "Unable to open file: " << fileName << std::endl;
        return 1;
    }

    //We basically assume that the file is formatted correctly for now
    int num;
    int currentRow = 0;
    while(currentRow < NUM_ROWS)
    {
        int currentCol = 0;
        while(currentCol < currentRow+1)
        {
            inputFile >> num;
            arr[currentRow][currentCol] = num;
            currentCol++;
        }
        currentRow++;
    }
    printArr(arr);
    bruteSolve(arr);
    //dynSolve(arr);


    //Delete each inner array
    for(int i=0; i<NUM_ROWS; i++)
    {
       delete[] arr[i]; 
    }
    delete[] arr;
    inputFile.close();
    return 0;
}

void bruteSolve(int** arr)
{
    int max = recSolve(arr, 0, 0);
    std::cout << "Answer: " << max << std::endl;
    return;
}

int recSolve(int** arr, int row, int col)
{
    // Break condition when it's in the last row of the pyramid
    if(row == NUM_ROWS-1)
    {
        return arr[row][col];
    }
    else
    {
        // This node's value plus max of left child node and right child node
        int max = arr[row][col] + std::max(recSolve(arr, row+1, col), recSolve(arr, row+1, col+1));
        return max;
    }
}

void dynSolve(int **arr)
{
    return;
}

void printArr(int **arr)
{
    int currentRow = 0;
    while(currentRow < NUM_ROWS)
    {
        int currentCol = 0;
        while(currentCol < currentRow+1)
        {
            std::cout << arr[currentRow][currentCol] << " ";
            currentCol++;
        }
        std::cout << std::endl;
        currentRow++;
    }
}
