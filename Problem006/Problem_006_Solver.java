/**
 * The sum of the squares of the first ten natural numbers is, 
 * 1^(2) + 2^(2) + ... + 10^(2) = 385
 * The square of the sum of the first ten natural numbers is,
 * (1 + 2 + ... + 10)^(2) = 55^(2) = 3025
 * Hence the difference between the sum of the squares of the first ten natural 
 * numbers and the square of the sum is 3025 - 385 = 2640.
 * 
 * Find the difference between the sum of the squares of the first one hundred 
 * natural numbers and the square of the sum.
 * 
 * Answer: "25164150"
 */

public class Problem_006_Solver 
{
	public static void main(String[] args)
	{
		int sumOfSqaures = sumOfSquares(100);
		int squareOfSum = squareOfSum(100);
		
		int difference = squareOfSum - sumOfSqaures;
		
		System.out.println(""+squareOfSum +"-"+ sumOfSqaures + "=" + difference);
	}
	
	public static int sumOfSquares(int upperLimit)
	{
		int sum = 0;
		for(int i=0; i<=upperLimit; i++)
		{
			sum += i*i;		
		}
		return sum;
	}
	
	public static int squareOfSum(int upperLimit)
	{
		int sum =0;
		for(int i=0; i<=upperLimit; i++)
		{
			sum+=i;
		}
		int retVal = sum*sum;
		return retVal;
	}
}
