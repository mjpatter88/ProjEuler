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
import java.lang.IllegalArgumentException;
import java.util.Iterator;

public class Problem_043_Solver
{
    public static int divisors[] = {17, 13, 11, 7, 5, 3, 2};
    public static boolean DEBUG = true;

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

        // make the first call
        filterDigits(digits, 0);

    }

    public static boolean filterDigits(Set<Integer> digits, int divisorIndex)
    {
        // Can you make a number 'length' digits long that is divisible by 'divisor[divisorIndex]'?
        // If no, return false.
        // If yes, remove those digits from the set, and call it on the next divisor.
        // If all numbers used, return true and then print which digits you used. (success)

        // This means success!
        if(digits.isEmpty())
        {
            return true;
        }
        if(divisorIndex >= divisors.length)
        {
            System.out.println("Problem! DivisorIndex = " + divisorIndex);
            throw new IllegalArgumentException();
        }
        int divisor = divisors[divisorIndex];
        while(divisor <= 999)
        {
            // check if divisor has all unique digits and each of those digits is in the 'digits' set.
            if(digitsInSet(digits, divisor))
            {
                if(DEBUG)
                {
                    System.out.print("Index: " + divisorIndex + " Divisor: " + divisor + " Digits in set: ");
                    printSet(digits);
                    System.out.println();
                }
                //Remove the used digits before making the recursive call
                removeDigitsFromSet(digits, divisor);
                // If the recursive call returns true, this is part of the solution!
                if(filterDigits(digits, divisorIndex+1))
                {
                    int[] solution = intToDigits(divisor);
                    for(int i=0; i<solution.length; i++)
                    {
                        System.out.print(solution[i]);
                    }
                }
                // Add in the digits we removed so we can keep looking
                addDigitsToSet(digits, divisor);
            }
            // Keep looking, we want to print all of the solutions.
            divisor += divisors[divisorIndex];
        }
        return false; // If we make it this far without a solution, return false.
    }

    // Returns true if each of the digits in 'number' is in the set
    public static boolean digitsInSet(Set<Integer> digits, int number)
    {
        int[] numberDigits = intToDigits(number);
        if(numberDigits[0] == numberDigits[1] || numberDigits[0] == numberDigits[2] ||
                numberDigits[1] == numberDigits[2])
        {
            return false;   // They must all be unique to be in the set by definition.
        }
        // Ugly, but works for our purposes
        return (digits.contains(numberDigits[0]) && digits.contains(numberDigits[1]) &&
                        digits.contains(numberDigits[2]));
    }

    public static void removeDigitsFromSet(Set<Integer> digits, int number)
    {
        int[] toRemove = intToDigits(number);
        for(int i=0; i<toRemove.length; i++)
        {
            digits.remove(toRemove[i]);
        }
    }

    public static void addDigitsToSet(Set<Integer> digits, int number)
    {
        int[] toAdd = intToDigits(number);
        for(int i=0; i<toAdd.length; i++)
        {
            digits.add(toAdd[i]);
        }
    }

    // Returns an array of ints that is the list of digits in 'number'
    // Automatically pads left with zeros if the number does not have 3 digits.
    // The subtraction of '0' is to convert the char ascii value to the int number.
    public static int[] intToDigits(int number)
    {
        int[] retDigits = new int[3];
        char[] digits = String.valueOf(number).toCharArray();
        if(digits.length == 1)
        {
            retDigits[0] = 0;
            retDigits[1] = 0;
            retDigits[2] = digits[0] - '0';
        }
        else if(digits.length == 2)
        {
            retDigits[0] = 0;
            retDigits[1] = digits[0] - '0';
            retDigits[2] = digits[1] - '0';
        }
        else if(digits.length == 3)
        {
            retDigits[0] = digits[0] - '0';
            retDigits[1] = digits[1] - '0';
            retDigits[2] = digits[2] - '0';
        }
        else
        {
            System.out.println("Problem in intsToDigits. Length: " + digits.length);
            throw new IllegalArgumentException();
        }
        return retDigits;
    }

    public static void printSet(Set<Integer> set)
    {
        Iterator<Integer> iter = set.iterator();
        while(iter.hasNext())
        {
            System.out.print(iter.next());
        }
    }

}
