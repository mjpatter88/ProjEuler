/**
 * If we list all the natural numbers below 10 that are multiples of 3 or 5, 
 * we get 3, 5, 6 and 9. The sum of these multiples is 23. 
 * Find the sum of all the multiples of 3 or 5 below 1000.
 * 
 * Answer: "233168"
 */

/**
 * This class attempts to solve problem 1 from Project Euler.
 * 
 * @author Michael Patterson
 *
 */
public class Problem_001_Solver 
{
	/**
	 * Entry point for this program.  Executes the main program flow.
	 * 
	 * @param args - Optional command line arguments
	 */
	public static void main(String[] args)
	{
		long startTime_nonOpt = System.currentTimeMillis();
		int answer_nonOpt = generateAnswer();
		long endTime_nonOpt = System.currentTimeMillis();
		
		long startTime_Opt = System.currentTimeMillis();
		int answer_Opt = opt_generateAnswer();
		long endTime_Opt = System.currentTimeMillis();
		
		
		//output the answers and times
		System.out.println("Non-optimized: " +answer_nonOpt + " Time:"
				+ (int)(endTime_nonOpt-startTime_nonOpt));
		System.out.println(answer_nonOpt);
		
		System.out.println("Optimized: " +answer_Opt + " Time:"
				+ (int)(endTime_Opt-startTime_Opt));
		System.out.println(answer_Opt);
	}
	
	/**
	 * Method that attempts to return the solution to problem 1
	 * 
	 * @return - The sum of all the multiples of 3 or 5 below 1000.
	 */
	public static int generateAnswer()
	{

		int sum = 0;
		
		for(int i=0; i<1000; i++)
		{
			if((i%3 == 0) | (i%5 == 0))
			{	//if i is a multiple of 3 or 5
				//add it to the current sum
				sum += i;
			}
		}
		return sum;
	}
	
	/**
	 * Optimized method that attempts to return the solution to problem 1.
	 * 
	 * @return - The sum of all the multiples of 3 or 5 below 1000.
	 */
	public static int opt_generateAnswer()
	{
		int sum = 0;
		
		int multOf3 = (3+999)*333/2;
		int multOf5 = (5+995)*199/2;
		int multOf15 = (990+15)*66/2;
		//subtract multiples of 15.
		sum = (multOf3+multOf5-multOf15);
		
		return sum;
	}
}
