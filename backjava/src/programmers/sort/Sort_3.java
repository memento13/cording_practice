package programmers.sort;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Sort_3 {
    public static void main(String[] args) {

        int[] citations = {3, 0, 6, 1, 5};
        int answer = 0;


        /**
         * 정렬후
         */
        List<Integer> citationsList = new ArrayList<>();
        for (int citation : citations) {
            citationsList.add(citation);
        }
        Collections.sort(citationsList,Collections.reverseOrder());
        int h;
        int above=0;
        for(int i=0;i<citationsList.size();i++){
            int below=0;
            for (int j =i+1;j<citationsList.size();j++) {


            }
//            if(h<below&&)
            above++;

        }



        System.out.println(answer);
    }

}
