package programmers.bruteforce;

import java.util.ArrayList;
import java.util.List;

public class BruteForce_1 {
    public static void main(String[] args) {

        int[] answers = {1,3,2,4,2};

        int[] answer = {};

        //수포자
        int[] one = {1, 2, 3, 4, 5};
        int[] two = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] three = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

        //각자 점수
        int[] score = {0,0,0};

        List<Integer> lstAnswer = new ArrayList<>();
        for (int i=0;i<answers.length;i++) {
            if(answers[i]==one[i%5]){
                score[0]++;
            }
            if(answers[i]==two[i%8]){
                score[1]++;
            }
            if(answers[i]==three[i%10]){
                score[2]++;
            }
        }

        int max=0;
        for (int i : score) {
            if(max<i){
                max=i;
            }
        }

        for(int i=0;i<score.length;i++){
            if(max==score[i]){
                lstAnswer.add(i+1);
            }
        }

        answer = new int[lstAnswer.size()];

        for(int i=0;i<lstAnswer.size();i++){
            answer[i]=lstAnswer.get(i);
        }
        for (int i : answer) {
            System.out.println(i);
        }
    }
}
