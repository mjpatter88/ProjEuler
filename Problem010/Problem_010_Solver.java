/**
 * The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. 
 * Find the sum of all the primes below two million.
 * 
 * Answer: "142913828922"
 */

/**
 * Resources: See Problem_003_Solver.java
 */

import java.util.ArrayList;

public class Problem_010_Solver 
{
	
	private ArrayList<Integer> primeNumbers;
	
	public Problem_010_Solver()
	{
		primeNumbers = new ArrayList<Integer>();
		//provide the first few known primes (2,3,5,7)
		primeNumbers.add(2);
		primeNumbers.add(3);
		primeNumbers.add(5);
		primeNumbers.add(7);
	}
	
	public void generateNextPrime()
	{
		//start guessing with the last prime already found.  It gets incremented
		//at the start of the loop
		int nextPrime = primeNumbers.get(primeNumbers.size()-1);
		boolean isPrime = false;
		while(!isPrime)
		{
			//increment by 2 so that it stays odd.
			nextPrime+=2;
			//check if this is a prime by dividing it by every smaller prime
			isPrime = true;
			
			//second method
			int curPos = 0;
			while(primeNumbers.get(curPos)*primeNumbers.get(curPos)<=nextPrime)
			{
				if(nextPrime % primeNumbers.get(curPos)==0)
				{
					isPrime = false;
					break;
				}
				curPos++;
			}
		}
		//at this point nextPrime must be a primeNumber
		primeNumbers.add(nextPrime);
	}
	
	
	public static void main(String[] args)
	{
		Problem_010_Solver test = new Problem_010_Solver();
		test.generateNextPrime();
		while(test.primeNumbers.get(test.primeNumbers.size()-1)<2000000)
		{//while the last element is less than 2000000
			test.generateNextPrime();
		}
		//remove the last element in the arrayList, because it is over 2 million
		test.primeNumbers.remove(test.primeNumbers.size()-1);
		//print out the last element in the array for debugging purposes
		System.out.println(test.primeNumbers.get(test.primeNumbers.size()-1));
		long sum =0;
		for(int i=0; i<test.primeNumbers.size(); i++)
		{
			sum += test.primeNumbers.get(i);
		}
		System.out.println(sum);
	}

}
