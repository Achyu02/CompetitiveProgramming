import java.util.Random;

class Solution {

    private static final Random rnd = new Random();

    private static int rand5() {
        return rnd.nextInt(5) + 1;
    }

    public static int rand7() {
         int temp = rand5()+rand5()*5 - 6;
        if(temp<21){
        return (temp%7)+1;
        }
        else{
            return rand7();
        }
    }

    public static void main(String[] args) {
        for (int i = 0; i < 14; i++) {
            System.out.printf("%d ", rand7());
        }
        System.out.println();
    }
}


