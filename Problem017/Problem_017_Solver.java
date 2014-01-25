import java.util.HashMap;

/**
 *
 * If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
 *
 * If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
 *
 * NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
 *
 * Answer = "21124"
 */

public class Problem_017_Solver
{
    /**
     * Thoughts:
     *      Some type of dynamic programming...
     *      Special cases: 10, 20, 30, 40, 50, 60, 70, 80, 90
     *      11, 12, 13, 14, 15, 16, 17, 18, 19
     *      1000
     *
     *      Idea 2:
     *      Calc based on digit, starting at the left?
     *      Recursive?
     *
     *      Idea 3:
     *      I think I'm making this too complicated. Create a map with the 40ish possibilities, then just use it.
     */

    private static HashMap<Integer, Integer> numToDigits;

    public static void main(String args[])
    {
        long startTime = System.nanoTime();

        init();
        int sumOfDigits = 0;
        for(int i=1; i<=1000; i++)
        {
            sumOfDigits += calcDigits(i);
        }
        System.out.println(sumOfDigits);


        long endTime = System.nanoTime();
        long seconds = (endTime - startTime)/1000000000;
        long milliseconds = ((endTime - startTime)%1000000000)/1000000;
        System.out.println("Calculation took: " + seconds + " seconds and " + milliseconds + " milliseconds.");
    }

    private static void init()
    {
        numToDigits = new HashMap<Integer, Integer>();
        numToDigits.put(1, 3);
        numToDigits.put(2, 3);
        numToDigits.put(3, 5);
        numToDigits.put(4, 4);
        numToDigits.put(5, 4);
        numToDigits.put(6, 3);
        numToDigits.put(7, 5);
        numToDigits.put(8, 5);
        numToDigits.put(9, 4);
        numToDigits.put(10, 3);
        numToDigits.put(11, 6);
        numToDigits.put(12, 6);
        numToDigits.put(13, 8);
        numToDigits.put(14, 8);
        numToDigits.put(15, 7);
        numToDigits.put(16, 7);
        numToDigits.put(17, 9);
        numToDigits.put(18, 8);
        numToDigits.put(19, 8);

        numToDigits.put(20, 6);
        numToDigits.put(30, 6);
        numToDigits.put(40, 5);
        numToDigits.put(50, 5);
        numToDigits.put(60, 5);
        numToDigits.put(70, 7);
        numToDigits.put(80, 6);
        numToDigits.put(90, 6);
        numToDigits.put(100, 10);
        numToDigits.put(200, 10);
        numToDigits.put(300, 12);
        numToDigits.put(400, 11);
        numToDigits.put(500, 11);
        numToDigits.put(600, 10);
        numToDigits.put(700, 12);
        numToDigits.put(800, 12);
        numToDigits.put(900, 11);
        numToDigits.put(1000, 11);
    }

    private static int calcDigits(int number)
    {
        if(numToDigits.containsKey(number))
        {
            return numToDigits.get(number);
        }
        else
        {
            //At this point we know it is not one of the special cases, now do hundreds, tens, ones

            int numDigits = 0;
            if(number > 100)
            {
                numDigits = 3; //"and" when saying hundred and tens etc.
                return numToDigits.get((number/100)*100) + calcDigits(number % 100) + 3;
                //Easy dynamic programming, add the return value to the map :)
            }
            else
            {
                //At this point we know the number is > 20 and < 100 and not a special case
                return numToDigits.get((number/10)*10) + calcDigits(number % 10);
            }
        }
    }
}