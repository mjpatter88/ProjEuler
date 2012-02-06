/**
 * By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
 * we can see that the 6^(th) prime is 13.
 * 
 * What is the 10001^(st) prime number?
 * 
 * Answer: "104743"
 */

import java.util.ArrayList;


//Note: reusing the generate primes method from problem_003
public class Problem_007_Solver 
{
	private ArrayList<Integer> primeNumbers;
	
	public Problem_007_Solver()
	{
		primeNumbers = new ArrayList<Integer>();
		//provide the first few known primes (2,3,5,7)
		primeNumbers.add(2);
		primeNumbers.add(3);
		primeNumbers.add(5);
		primeNumbers.add(7);
	}
	
	
	public static void main(String[] args)
	{
		Problem_007_Solver test = new Problem_007_Solver();
		
		while(test.primeNumbers.size()<=10000)
		{
			test.generateNextPrime();
		}
		System.out.println(test.primeNumbers.get(10000));
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
			int curPos = 0;
			
			//second method
			while(primeNumbers.get(curPos)*primeNumbers.get(curPos)<=nextPrime)
			{
				if(nextPrime % primeNumbers.get(curPos)==0)
				{
					isPrime = false;
					break;
				}
				curPos++;
			}
			
			/*
			//first method
			for(int i=0; i<primeNumbers.size(); i++)
			{
				if(nextPrime % primeNumbers.get(i) == 0)
				{
					isPrime = false;
					break;
				}
			}
			*/
			
		}
		//at this point nextPrime must be a primeNumber
		primeNumbers.add(nextPrime);
	}
}
