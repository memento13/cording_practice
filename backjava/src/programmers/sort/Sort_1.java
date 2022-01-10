package programmers.sort;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Sort_1 {
    public static void main(String[] args) {
        /**
         *
         * 출력요구사항
         */

        int[] array=
                {1, 5, 2, 6, 3, 7, 4};
        int[][] commands =
                {{2, 5, 3}, {4, 4, 1}, {1, 7, 3}};

        int[] answer = {};

        answer = new int[commands.length];
        int idx=0;

        for (int[] command : commands) {
            List<Integer> lst = new ArrayList<>();
            int start = command[0]-1;
            int end = command[1];
            int findIndex = command[2]-1;
            for(int arrIdx = start; arrIdx<end;arrIdx++){
                lst.add(array[arrIdx]);
            }
            Collections.sort(lst);
            answer[idx] = lst.get(findIndex);
            idx++;
        }


        for (int i : answer) {
            System.out.print( i+", ");
        }
    }
}
