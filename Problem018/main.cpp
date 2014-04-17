/*
 * Answer: 1074
 */
#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>

#define NUM_ROWS 15
#define DEBUG false

void bruteSolve(int** arr);
void dynSolve(int **arr);
void bottomUpSolve(int **arr);

void printArr(int **arr);
int recBrute(int** arr, int row, int col);

int main(int argc, char* argv[])
{
    /*
     * For now we will be using jagged 2D arrays for lack of a better data structure.
     * I'll write 3 different functions utilizing different methods.     
     * 1) Slow brute force method "bruteSolve"
     * 2) Faster dynamic programming method "dynSolve"
     * 3) Clever bottom-up summing method "bottomUpSolve"
     */

    //First handle command line parameters
    void (*pSolve)(int**) = bottomUpSolve;
    if(DEBUG)
    {
        std::cout << "Command line args: " << argc << std::endl;
    }
    if(argc > 1)
    {
        if(std::string("-h").compare(argv[1]) == 0)
        {
            std::cout << "Usage: ./main [flags]" << std::endl;
            std::cout << "\t-b for brute force solution" << std::endl;
            std::cout << "\t-d for dynamic programming solution" << std::endl;
            std::cout << "\t-c for a clever bottom up solution (default)" << std::endl;
            return 0;
        }
        else if(std::string("-b").compare(argv[1]) == 0)
        {
            pSolve = bruteSolve;
        }
        else if(std::string("-d").compare(argv[1]) == 0)
        {
            pSolve = dynSolve;
        }
        else if(std::string("-c").compare(argv[1]) == 0)
        {
            pSolve = bottomUpSolve;
        }
    }

    //First we need an array of pointers
    int** arr = new int*[NUM_ROWS];
    for(int i=0; i<NUM_ROWS; i++)   //Create each inner array
    {
        arr[i] = new int[i+1];  //Each row has one more element than the previous
    }

    //Fill the arrays with the numbers from the file.
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

    if(DEBUG)
    {
        printArr(arr);
    }

    pSolve(arr);
    //bruteSolve(arr);
    //dynSolve(arr);
    //bottomUpSolve(arr);


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
    if(DEBUG)
    {
        std::cout << "Brute force soltuion..." << std::endl;
    }
    int max = recBrute(arr, 0, 0);
    std::cout << "Answer: " << max << std::endl;
    return;
}

int recBrute(int** arr, int row, int col)
{
    // Break condition when it's in the last row of the pyramid
    if(row == NUM_ROWS-1)
    {
        return arr[row][col];
    }
    else
    {
        // This node's value plus max of left child node and right child node
        int max = arr[row][col] + std::max(recBrute(arr, row+1, col), recBrute(arr, row+1, col+1));
        return max;
    }
}

void dynSolve(int **arr)
{
    if(DEBUG)
    {
        std::cout << "Dynamic programming soltuion..." << std::endl;
    }
    return;
}

void bottomUpSolve(int **arr)
{
    if(DEBUG)
    {
        std::cout << "Clever bottum-up soltuion..." << std::endl;
    }
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
