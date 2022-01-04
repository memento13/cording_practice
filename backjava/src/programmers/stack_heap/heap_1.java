package programmers.stack_heap;

import java.util.PriorityQueue;

public class heap_1 {
    public static void main(String[] args) {
        int[] scoville=
                {1, 2, 3, 9, 10, 12};
        int K=
                7;
        int answer = 0;

        /**
         * 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
         * 우선순위큐 선언 -> 주입
         * 반복문시작--
         * 만약 poll한 음식이 K보다 높은경우 : 반복문 끝
         * answer ++
         * 먼저 poll한 음식+(poll한 음식 *2) 다시 큐에 add
         * 반복문 끝--
         * answer 반환
         */
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>();
        for (int food : scoville) {
            priorityQueue.add(food);
        }
        while (true){
            Integer firstFood = priorityQueue.poll();
            if(firstFood>=K){
                break;
            }
            if(priorityQueue.isEmpty()){
                answer = -1;
                break;
            }
            answer++;
            Integer secondFood = priorityQueue.poll();
            priorityQueue.add(firstFood+(secondFood*2));
        }

        System.out.println("answer = " + answer);
    }
}

