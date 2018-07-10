class Solution
{
	static int max(int a, int b) { return (a > b)? a: b; }
	static int eggThrown(int n, int k)
	{
		int floor[][] = new int[n+1][k+1];
		int temp;
		int i, j, x;		
		for (i = 1; i <= n; i++)
		{
			floor[i][1] = 1;
			floor[i][0] = 0;
		}
		for (j = 1; j <= k; j++)
			floor[1][j] = j;

		for (i = 2; i <= n; i++)
		{
			for (j = 2; j <= k; j++)
			{
				floor[i][j] = Integer.MAX_VALUE;
				for (x = 1; x <= j; x++)
				{
					temp = 1 + max(floor[i-1][x-1], floor[i][j-x]);
					if (temp < floor[i][j])
						floor[i][j] = temp;

				}
			}
		}
		return floor[n][k];

	}
		
	public static void main(String args[] )
	{
		System.out.println(eggThrown(2,10));
		System.out.println(eggThrown(2,4));
		System.out.println(eggThrown(2,8));
		System.out.println(eggThrown(2,50));
		System.out.println(eggThrown(2,100));
		 
	}
}
