package programmers.hash;

import java.util.*;

public class hash_3 {

    public static void main(String[] args) {

        String[][] clothes =
//                {{"crowmask", "face"}, {"bluesunglasses", "face"}, {"smoky_makeup", "face"}};
                
                {{"yellowhat", "headgear"}, {"bluesunglasses", "eyewear"}, {"green_turban", "headgear"}};
        int answer = 0;

        Map<String, Integer> map = new HashMap<>();
        for (String[] strings : clothes) {
            if(!map.containsKey(strings[1])){
                map.put(strings[1],1);
            }
            else {
                map.put(strings[1],map.get(strings[1])+1);
            }
        }
        Collection<Integer> values = map.values();
        List<Integer> valueList = new ArrayList<>(values);

        int typeOfClothes =1;
        for (Integer clothesCnt : valueList) {
            typeOfClothes *= clothesCnt+1; //1 더하는 이유는 해당 옷을 안 입는 경우
        }
        answer = typeOfClothes-1;//아에 안입는 경우

        System.out.println("answer = " + answer);


    }
}
