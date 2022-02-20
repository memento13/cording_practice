package programmers.bruteforce;

public class BruteForce_3 {

    public static void main(String[] args) {

        int brown = 10;
        int yellow = 2;

        int[] answer = {};

        answer = finder(brown,yellow,1);



        System.out.println("answer = " + answer[0]+" "+answer[1]);
    }

    public static int[] finder(int brown,int yellow, int row){
        //공약수 문제..
        if(yellow%row==0){
            int col = yellow/row;
            if(brown == (row*2)+(col*2)+4){
                int[] result = {col+2,row+2};
                return result;
            }
        }

        return finder(brown,yellow,row+1);
    }
}
