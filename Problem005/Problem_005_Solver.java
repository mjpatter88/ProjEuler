/**
 * 2520 is the smallest number that can be divided by each of the numbers 
 * from 1 to 10 without any remainder. 
 * 
 * What is the smallest number that is evenly divisible 
 * by all of the numbers from 1 to 20?
 * 
 * Answer: "232792560"
 */

public class Problem_005_Solver 
{
	public static void main(String[] args)
	{
		int number = 20;
		
		while(!isSolution(number))
		{
			number+=20;
		}
		System.out.println(number);
	}
	
	public static boolean isSolution(int number)
	{
		boolean retVal = true;
		for(int i=1; i<=20; i++)
		{
			if(number%i!=0)
			{
				retVal=false;
				break;
			}
		}
		return retVal;
	}
}
