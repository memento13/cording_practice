package programmers;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class kakaoIntern_1 {
    public static void main(String[] args) {
        String s ="one4seveneight";
        int answer = 0;

//================================================================================ 헛짓거리였음
        Map<String,Integer> mapNumbers = new HashMap<>();
        Set<String> numbers = new HashSet<>();
        String[] strNumbers = {"zero","one","two","three","four","five","six","seven","eight","nine"};
        for(int i=0;i<10;i++){
            numbers.add(Integer.toString(i));
            mapNumbers.put(strNumbers[i],i);
        }
        StringBuffer result = new StringBuffer();
        StringBuffer strNumber = new StringBuffer();

        for (char c : s.toCharArray()) {
            String value = String.valueOf(c);
            if(numbers.contains(value)){
                result.append(value);
            }
            else{
                strNumber.append(value);
                if(mapNumbers.containsKey(strNumber.toString())){
                    result.append(mapNumbers.get(strNumber.toString()));
                    strNumber = new StringBuffer();
                }
            }
        }
        answer = Integer.parseInt(result.toString());
//================================================================================

        //         replaceAll을 쓰면 다 되는거였다.
        String[] digits = {"0","1","2","3","4","5","6","7","8","9"};
        String[] alphabets = {"zero","one","two","three","four","five","six","seven","eight","nine"};

        for(int i=0; i<10; i++){
            s = s.replaceAll(alphabets[i],digits[i]);
        }
        answer = Integer.parseInt(s);
        System.out.println("answer = " + answer);
    }
}
