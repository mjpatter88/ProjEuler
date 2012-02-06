/**
 * A palindromic number reads the same both ways. The largest palindrome 
 * made from the product of two 2-digit numbers is 9009 = 91 × 99. 
 * 
 * Find the largest palindrome made from the product of two 3-digit numbers.
 * 
 * Answer: "906609"
 */

import java.util.ArrayList;
import java.util.Collections;

public class Problem_004_Solver 
{
	
	
	public static void main(String[] args)
	{
		ArrayList<Integer> answers = new ArrayList<Integer>();
		
		int number1 = 999;
		int number2 = 999;
		int product = 0;
		while(number1>100)
		{
			
			
			product = number1*number2;
			if(checkForPalindrome(product))
			{
				answers.add(product);
			}
			
			if(number2==100)
			{
				number1--;
				number2 = number1;
			}
			else
			{
				number2--;
			}
			
		}
		
		Collections.sort(answers);
		for(int i=0; i<answers.size(); i++)
		{
			System.out.println(answers.get(i));
		}
	}
	
	/**
	 * Checks if the provided number is a palindrome.  A number is a palindrome
	 * if it reads the same forwards and backwards.  Example: 101
	 * 
	 * @param number - The number to be checked for palindromic characteristics.
	 * @return - True if the number is a palindrome, false if it is not.
	 */
	public static boolean checkForPalindrome(int number)
	{
		String numString = ""+number;
		boolean retVal = true;
		int firstIndex = 0;
		int secondIndex = numString.length()-1;
		while(firstIndex<secondIndex)
		{
			if(numString.charAt(firstIndex)!=numString.charAt(secondIndex))
			{
				retVal = false;
				break;
			}
			firstIndex++;
			secondIndex--;
		}
		
		return retVal;
	}
}
