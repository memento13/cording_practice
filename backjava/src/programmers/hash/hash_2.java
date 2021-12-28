package programmers.hash;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;

public class hash_2 {
    public static void main(String[] args) {
        boolean answer = true;
        Map<String, Integer> map = new HashMap<>();
        String[] arr = {"123","456","789"};
        for (String s : arr) {
            map.put(s,Integer.parseInt(s));
        }


        for (String s : arr) {
            for( int j = 0; j<s.length();j++){
                if(map.containsKey(s.substring(0,j))){
                    answer =false;
                    break;
                }
            }
            if (!answer){
                break;
            }
        }
        System.out.println(answer);

    }
}
