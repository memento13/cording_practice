package programmers.greedy;

import java.util.Arrays;
import java.util.HashMap;

public class greedy_1 {

    public static void main(String[] args) {

        int n = 5;
        int[] lost = {2,3,4};
        int[] reserve = {1,2,3};

        /**
         * 여분학생중 도난 체크해서 여분에서제외
         * 체육 가능학생(cnt) n-lost.length
         * 도난학생-1이 여분을 가지고 있으면 cnt++
         * 없다면 도난학생 +1에서 가져오고 cnt++
         * 둘다 없다면 넘어감
         * 여분에서 번호 제외 (안해도 될듯)...
         */


        int answer = 0;

        Arrays.sort(lost);
        Arrays.sort(reserve);

        answer = n-lost.length;
        //여분 기록
        HashMap<Integer, Boolean> reserveMap = new HashMap<>();
        for (int i : reserve) {
            reserveMap.put(i,true);
        }
        //도난 기록
        HashMap<Integer, Boolean> lostMap = new HashMap<>();
        for (int i : lost) {
            lostMap.put(i,true);
        }

        //여분학생중 도난체크
        for (int i : lost) {
            if(reserveMap.get(i)!=null && reserveMap.get(i)==true){
                answer++;
                reserveMap.put(i,false);
                lostMap.put(i,false);
            }
        }

        for (int i : lost) {
            //도난 상태인가?
            if(lostMap.get(i)!=null && lostMap.get(i)==true){
                //자기 앞번호가 여분이 있는가?
                if(reserveMap.get(i-1)!=null && reserveMap.get(i-1)==true){
                    answer++;
                    lostMap.put(i,false);
                    reserveMap.put(i-1,false);
                }
                else if(reserveMap.get(i+1)!=null && reserveMap.get(i+1)==true){
                    answer++;
                    lostMap.put(i,false);
                    reserveMap.put(i+1,false);
                }
            }
        }

        System.out.println("answer = " + answer);
    }
}
