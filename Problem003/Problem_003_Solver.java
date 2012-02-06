/**
 * The prime factors of 13195 are 5, 7, 13 and 29. 
 * 
 * What is the largest prime factor of the number 600851475143 ?
 * 
 * Answer: "6857"
 */

/**
 * Resources:
 * http://www.purplemath.com/modules/factnumb.htm
 * http://mathforum.org/library/drmath/sets/select/dm_prime_factors.html
 * 
 * http://mathforum.org/library/drmath/view/57072.html
 * http://mathforum.org/dr.math/faq/faq.prime.num.html
 * 
 * http://mathforum.org/dr.math/faq/faq.divisibility.html
 * http://mathforum.org/k12/mathtips/division.tips.html#divide13
 */

import java.util.ArrayList;

public class Problem_003_Solver 
{
	private ArrayList<Integer> primeNumbers;
	private ArrayList<Integer> primeFactors;
	
	public Problem_003_Solver()
	{
		primeNumbers = new ArrayList<Integer>();
		primeFactors = new ArrayList<Integer>();
		
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
			/*
			//first method
			for(int i=0; i<primeNumbers.size(); i++)
			{
				if(nextPrime % primeNumbers.get(i) == 0)
				{
					isPrime = false;
				}
			}
			*/
		}
		//at this point nextPrime must be a primeNumber
		primeNumbers.add(nextPrime);
	}
	
	public void findPrimeFactors(long number)
	{
		long numberRemaining = number;
		//the largest factor squared must be smaller than the number
		int i = 0;	//index of the prime we are trying as a factor
		while(primeNumbers.get(i)*primeNumbers.get(i) < numberRemaining)
		{
			if(numberRemaining % primeNumbers.get(i) == 0)
			{
				primeFactors.add(primeNumbers.get(i));
				numberRemaining = numberRemaining/primeNumbers.get(i);
				System.out.println("Prime factor found! "+primeNumbers.get(i));
				System.out.println("Remaining number = "+numberRemaining);
			}
			
			i++;
			
			if(i>=primeNumbers.size())
			{
				generateNextPrime();
			}
		}
		if(numberRemaining>1)
		{
			primeFactors.add((int)numberRemaining);
		}
		
	}
	
	
	
	public static void main(String[] args)
	{
		Problem_003_Solver test = new Problem_003_Solver();
		//generate and print the first 1000 primes.
		long testNumber = 600851475143L;
		test.findPrimeFactors(testNumber);
		
		for(int i=0; i<test.primeFactors.size(); i++)
		{
			System.out.println(""+test.primeFactors.get(i)+", ");
		}
	}
}
