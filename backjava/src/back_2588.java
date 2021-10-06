import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.SQLOutput;


public class back_2588 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input1 = br.readLine();
        String input2 = br.readLine();

        int a = Integer.parseInt(input1);
        int b = Integer.parseInt(input2);

        int[] nums = new int[input2.length()];

        for(int i = 0; i < input2.length(); i++){
            nums[input2.length()-i-1] = input2.charAt(i) - '0';
        }

        System.out.println(a*nums[0]);
        System.out.println(a*nums[1]);
        System.out.println(a*nums[2]);
        System.out.println(a*b);
    }

}
