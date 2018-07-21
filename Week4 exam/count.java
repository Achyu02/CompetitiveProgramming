import java.util.*;
class count {
    static int decToBinary(int n)
    {
        int[] binary = new int[1000];
  	int c=0;
      int i = 0;
        while (n > 0) 
        {
            binary[i] = n % 2;
            n = n / 2;
            i++;
        }
          for (int j = i - 1; j >= 0; j--)
          {
            if(binary[j]==1){
            	c=c+1;
            }
            else{
            	continue;
            }
        }
        return c;
    }
    static void numbercount(int n){
		 int[] result=new int[n+1];
		 for (int i=0;i<=n;i++) {
		 	// System.out.println(i);
		 	result[i]=decToBinary(i);
		 }
		 System.out.println(Arrays.toString(result));
 	
    }
	public static void main(String[] args) {
		numbercount(15);
		numbercount(16);
		numbercount(1);
		numbercount(25);
		numbercount(5);
		numbercount(6);
		 
		
	}
	
}