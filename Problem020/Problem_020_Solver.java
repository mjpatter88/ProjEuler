import java.math.BigDecimal;
import java.math.BigInteger;

/**
 *
 * n! means n × (n − 1) × ... × 3 × 2 × 1
 *
 * For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
 * and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
 *
 * Find the sum of the digits in the number 100!
 *
 * Answer = "648"
 */


public class Problem_020_Solver
{

    /**
     * Java BigInt?
     *
     */

    public static void main(String args[])
    {
        long startTime = System.nanoTime();

        BigInteger result = new BigInteger("1");
        for(int i=100; i>1; i--)
        {
            result = result.multiply(new BigInteger(String.valueOf(i)));
            System.out.println(result);
        }

        String resultString = result.toString();
        int sum = 0;
        for(int i=0; i < resultString.length(); i++)
        {
            sum += Integer.parseInt(String.valueOf(resultString.charAt(i)));    //There's gotta be a better way to do this...
        }
        System.out.println("Answer: " + sum);

        long endTime = System.nanoTime();
        long seconds = (endTime - startTime)/1000000000;
        long milliseconds = ((endTime - startTime)%1000000000)/1000000;
        System.out.println("Calculation took: " + seconds + " seconds and " + milliseconds + " milliseconds.");
    }
}