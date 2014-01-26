import java.util.ArrayList;

/**
 *
 * Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
 * If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
 *
 * For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
 *
 * Evaluate the sum of all the amicable numbers under 10000.
 *
 * Sources:
 *          1) http://en.wikipedia.org/wiki/Amicable_numbers
 *          2) http://britton.disted.camosun.bc.ca/amicable.html
 *
 * Answer = ""
 *
 */


public class Problem_021_Solver
{
    /**
     * Idea: Use the formula from the second link in the sources section.
     * When n=1, pair is (220, 284)
     *
     * This formula generated pairs correctly, but it seems that it doesn't generate all of them.
     *
     * New Idea: Brute force way?
     */

    public static void main(String args[])
    {

        long startTime = System.nanoTime();

        ArrayList<Integer> amicNumbers = new ArrayList<Integer>();

        for(int i=1; i<14; i++)
        {
            if(condition1(i) && condition2(i) && condition3(i))
            {
                // 2^(n+1) * (3*(2^n) - 1) * (3*2^(n+1)-1)
                // 2^(n+1) * ((3^2) * 2^(2*n+1) - 1)
                double num1 = Math.pow(2.0, (i+1)) * (3*(Math.pow(2.0, i))-1) * (3*Math.pow(2.0, (i+1))-1);
                double num2 = Math.pow(2.0, (i+1)) * (Math.pow(3.0, 2.0) * Math.pow(2.0, (2*i+1)) -1);
                amicNumbers.add((int) num1);
                amicNumbers.add((int) num2);
                System.out.println("Pair Found: " + num1 + ", " + num2);
            }
            else
            {
                //System.out.println(i);
            }
        }

        long endTime = System.nanoTime();
        long seconds = (endTime - startTime)/1000000000;
        long milliseconds = ((endTime - startTime)%1000000000)/1000000;
        System.out.println("Calculation took: " + seconds + " seconds and " + milliseconds + " milliseconds.");
    }

    private static boolean condition1(int i)
    {
        // 3*(2^n) - 1
        int num = (int) ((3) * Math.pow(2.0, i) - 1);
        //System.out.println("num1: " + num);
        return isPrime(num);
    }

    private static boolean condition2(int i)
    {
        // 3*2^(n+1)-1
        int num = (int) (int) ((3) * Math.pow(2.0, i+1) - 1);
        //System.out.println("num2: " + num);
        return isPrime(num);
    }

    private static boolean condition3(int i)
    {
        // (3^2)*2^(2n+1)-1
        int num = (int) (int) ((9) * Math.pow(2.0, 2*i+1) - 1);
        //System.out.println("num3: " + num);
        return isPrime(num);
    }

    /**
     * We'll do this the easy way for now, maybe use a sieve later...
     */
    private static boolean isPrime(int num)
    {
        if((num % 2) == 0)
        {
            return false;
        }

        //Check each odd number up to the square root of num.
        for(int i=3; i*i<num; i+=2)
        {
            if((num % i) == 0)
            {
                return false;
            }
        }

        return true;
    }




}
