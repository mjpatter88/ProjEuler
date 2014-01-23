/**
 * The following iterative sequence is defined for the set of positive integers:
 *
 * n → n/2 (n is even)
 * n → 3n + 1 (n is odd)
 *
 * Using the rule above and starting with 13, we generate the following sequence:
 * 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
 *
 * It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
 *
 * Which starting number, under one million, produces the longest chain?
 *
 * NOTE: Once the chain starts the terms are allowed to go above one million.
 *
 * Answer = "837799"
 */

public class Problem_014_Solver
{
    public static void main(String args[])
    {
        long startTime = System.nanoTime();

        calcAnswer(1000000);

        long endTime = System.nanoTime();
        long seconds = (endTime - startTime)/1000000000;
        long milliseconds = ((endTime - startTime)%1000000000)/1000000;
        System.out.println("Calculation took: " + seconds + " seconds and " + milliseconds + " milliseconds.");
    }

    private static void calcAnswer(int upperBound)
    {
        //Recursive way
        int lengthOfLongest = 0;
        int longestStartingVal = 0;
        for(int i=1; i<upperBound; i++)
        {
            int length = rec_Calc(i);
            if(length > lengthOfLongest)
            {
                lengthOfLongest = length;
                longestStartingVal = i;
            }
            //System.out.println(i);
        }
        System.out.println("\n");
        System.out.println("Answer: " + longestStartingVal);
        System.out.println("Length: " + lengthOfLongest);
        System.out.println("\n");

        //Dynamic way
    }

    private static int rec_Calc(long i) //When I started I used "int" instead of "long" and got the wrong answer.
    {
        if(i <= 1)
        {
            return 1;
        }
        else if(i%2 == 0)    //if i is even
        {
            return rec_Calc(i/2) + 1;
        }
        else
        {
            return rec_Calc(i*3 + 1) + 1;
        }
    }
}
