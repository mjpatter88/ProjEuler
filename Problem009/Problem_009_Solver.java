/**
 * A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, 
 * a^(2) + b^(2) = c^(2)
 * 
 * For example, 3^(2) + 4^(2) = 9 + 16 = 25 = 5^(2).
 * 
 * There exists exactly one Pythagorean triplet for which a + b + c = 1000.
 * Find the product abc.
 * 
 * Answer: "31875000"
 */

/**
 * Resources:
 * http://www.math.uic.edu/~fields/puzzle/triples.html
 */

public class Problem_009_Solver 
{
	public static void main(String[] args)
	{
		int a = 1;
		int b = 1;
		double c = 1;
		while(Math.abs((a+b+c)-1000) >=.0005)
		{
			if((a+b+c)>1000)
			{
				b = a;
				a++;
			}
			b++;
			c = Math.sqrt((a*a) + (b*b));
			System.out.println("a:"+a+" b:"+b+" c:"+c+" sum:"+(a+b+c));
		}
		System.out.println("a:"+a+" b:"+b+" c:"+c+" product:"+(a*b*c));
		System.out.println(Math.abs((a+b+c)-1000));
	}
}
