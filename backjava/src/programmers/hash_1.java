package programmers;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class hash_1 {
    public static void main(String[] args) {
        Map<String, Integer> map = new HashMap<>();
        String[] arr = {"jack","jack", "kim","lee"};
        for (String s : arr) {
            if(!map.containsKey(s)){
                map.put(s,1);
            }
            else {
                map.put(s,map.get(s)+1);
            }
        }
        for (String s : map.keySet()) {
            System.out.print("s = " + s);
            System.out.println("map.get(s) = " + map.get(s));
        }
        String[] arr2 = {"jack", "kim","lee"};
        for (String s : arr2) {
            map.put(s,map.get(s)-1);
        }
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            if(entry.getValue()==1){
                System.out.println("entry.getKey() = " + entry.getKey());
                break;
            }
        }


    }
}
