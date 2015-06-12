/*
 * Problem 43:
 *
 * The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the 
 * digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
 *
 * Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
 *
 *  d2d3d4=406 is divisible by 2
 *  d3d4d5=063 is divisible by 3
 *  d4d5d6=635 is divisible by 5
 *  d5d6d7=357 is divisible by 7
 *  d6d7d8=572 is divisible by 11
 *  d7d8d9=728 is divisible by 13
 *  d8d9d10=289 is divisible by 17
 *
 * Find the sum of all 0 to 9 pandigital numbers with this property.
 *
 *
 *
 * Thoughts: The first digit really doesn't matter, does it?
 * We're just checking 234, 345, 456, etc, never 1.
 * Also, the number of options are 9 permutations of 10, really partial permutations
 * 10! / (10-9)! options = 10! = 3,628,800 
 *
 * I think this should be brute-force able... especially using tricks like d4 must be even, etc.
 * Could I work backwards? There can't be many combinations divisible by 17, or 13, or 11...
 *
 */

import java.util.Set;
import java.util.HashSet;

public class Problem_043_Solver
{
    public int divisors[] = {17, 13, 11, 7, 5, 3, 2};

    public static void main(String args[])
    {
        System.out.println("Solving Project Euler Problem 43...");
        // Basic idea
        //
        // Given all 10 digits, filter backwards
        // What three can make numbers divisible by 17. 
        // Take those out, then check divisible by 13, then 11, etc.
        // Recursive?
        
        // try using a set...
        Set<Integer> digits = new HashSet<Integer>();
        for(int i=0; i<10; i++)
        {
            digits.add(i);
        }
    }

    public static boolen filterDigits(Set digits, int length, int divisorIndex)
    {
        // Can you make a number 'length' digits long that is divisible by 'divisor[divisorIndex]'?
        // If no, return false.
        // If yes, remove those digits from the set, and call it on the next divisor.
        // If all numbers used, return true and print which digits you used. (success)

        // This means success!
        if(digits.isEmpty())
        {
            return true;
        }
        else
        {
            int divisor = divisors[divisorIndex];
            while(divisor <= 999)
            {
                //TODO: check if divisor has all unique digits and each of those digits is in the 'digits' set.
                divisor += divisor;
            }
        }
        return false;
    }

}
