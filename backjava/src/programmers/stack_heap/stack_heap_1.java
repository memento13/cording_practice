package programmers.stack_heap;

import java.util.*;

public class stack_heap_1 {
    public static void main(String[] args) {
        int[] progresses; int[] speeds;
        progresses = new int[]
//                {93, 30, 55};
                {95, 90, 99, 99, 80, 99};
        speeds = new int[]
//                {1, 30, 5};
                {1, 1, 1, 1, 1, 1};


        Solution solution = new Solution();
        int[] answer = solution.solution(progresses,speeds);

        for (int i : answer) {
            System.out.println("i = " + i);
        }

    }


}
class Solution{
    /**
     * 100-progress 를 하여 남은 작업량 계산
     * 남은 작업량 / speed + if(남은작업량%speed)인 경우+1 = 배포예정일
     * 앞보다 배포예정일이 작은경우 배포갯수 ++
     * 앞의 배포 예정일보다 큰 경우 그동안 쌓인 배포의 갯수를 queue에 저장
     * queue에 answer 배열 재정의 후 값저장
     */
    public int[] solution(int[] progresses, int[] speeds){
        int[] answer = {};
        Queue<Integer> distQueue = null;
        distQueue = fillDistQueue(progresses, speeds);
        answer = fillAnswer(distQueue);
        return answer;
    }
    private static int[] fillAnswer( Queue<Integer> distQueue) {
        int[] answer = new int [distQueue.size()];
        for(int i =0;i<answer.length;i++){
            answer[i] = distQueue.poll();
        }
        return answer;
    }

    private static Queue<Integer> fillDistQueue(int[] progresses, int[] speeds) {
        Queue<Integer> distQueue = new LinkedList<>();
        int distDay = 0; //지금까지 선행작업중 가장 늦은 배포 예정일
        int distProgresses = 0; //배포할 작업의 갯수
        int distTime; //현재 작업의 배포 예정일

        for(int i=0;i<progresses.length;i++){
            distTime = getDistTime(progresses[i], speeds[i]);
            if(distTime>distDay){ //앞의 배포 예정일보다 큰 경우
                distQueue.add(distProgresses); //그동안 쌓인 배포의 갯수를 queue에 저장
                distDay = distTime;
                distProgresses =1;
            }
            else { //앞보다 배포예정일이 작은경우
                distProgresses++;
            }
        }
        distQueue.add(distProgresses); //남은 배포 저장
        distQueue.poll();//처음 배포 0 삭제
        return distQueue;
    }

    private static int getDistTime(int progress, int speed) {
        int restProgress;
        int distTime;
        restProgress= (100 - progress);
        distTime = restProgress/speed;
        if(restProgress%speed>0){
            distTime++;
        }
        return distTime;
    }
}
