import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;

public class back_1157 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        str = str.toUpperCase();
        char[] chars = str.toCharArray();

        int[] index = new int[26];
        for(char tmp : chars){
            index[tmp - 65]++;
        }

        int maxIndex = 0;
        int maxIndexCount = 0;
        int maxValue = index[0];

        for(int i=1;i<26;i++){
            if(index[i]>maxValue){
                maxIndexCount = 0;
                maxIndex=i;
                maxValue=index[i];
            }
            else if(index[i]==maxValue){
                maxIndexCount++;
            }
        }

        if(maxIndexCount>0){
            System.out.println("?");
        }
        else{
            System.out.println((char)(maxIndex+65));
        }

    }
}
