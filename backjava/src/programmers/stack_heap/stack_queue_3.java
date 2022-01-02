package programmers.stack_heap;

import java.util.LinkedList;
import java.util.Queue;

public class stack_queue_3 {
    public static void main(String[] args) {
        int bridge_length=
//                2;
                100;
        int weight =
//                10;
                100;

        int[] truck_weights =
//                {7,4,5,6};
                {10,10,10,10,10,10,10,10,10,10};
        int answer = 0;
        /**
         * 다리 객체 생성
         * 처음에 무게가 0인 트럭을 다리 길이만큼 다리에 집어넣음
         * 반복문 시작---
         * 매 시간 트럭 출차되고 들어올 수 있는지 체크함 (큐여서 poll시 다리위 모든 트럭이앞으로 감)
         * 트럭이 들어올 수 있다면 들어감 / 못들어가면 차간거리 용으로 무게 0짜리 트럭 진입
         * 반복문 끝---
         * 트럭이 다 들어가면 다리위에 마지막 트럭의 남은 다리거리만큼 시간+ 해줌
         */

        Bridge bridge = new Bridge(weight,bridge_length);
        for (int truck : truck_weights) {
            while (true){
                answer++;
                bridge.bridgeExit();
                if (bridge.isBridgeEnterAble(truck)){
                    bridge.bridgeEntrance(truck);
                    break;
                }
            }
        }
        answer+=bridge.remainingDistanceOnLastTruckOnBridge();

        System.out.println("answer = " + answer);
    }
}

class Bridge{
    private Queue<Integer> bridgeQue;
    private int weight;
    private int bridge_length;

    public Bridge(int weight,int bridge_length) {
        this.bridgeQue = new LinkedList<>();
        for(int i=0;i<bridge_length;i++){
            bridgeQue.add(0);
        }
        this.weight = weight;
        this.bridge_length = bridge_length;
    }

    public boolean isBridgeEnterAble(int truck){
        if(totalWeightTrucksOnBridge()+truck<=weight && bridgeQue.size()+1<=bridge_length){
            return true;
        }
        else{
            bridgeQue.add(0);
            return false;
        }
    }
    public void bridgeEntrance(int truck){
        bridgeQue.add(truck);
    }
    public void bridgeExit(){
        bridgeQue.poll();
    }
    public int totalWeightTrucksOnBridge(){
        int totalWeight = 0;
        for (Integer truck : bridgeQue) {
            totalWeight+=truck;
        }
        return totalWeight;
    }
    public int remainingDistanceOnLastTruckOnBridge(){
        return bridgeQue.size();
    }

//    public void printBridge(){
//        System.out.println("bridgeQue = " + bridgeQue);
//        System.out.println("totalWeightTrucksOnBridge() = " + totalWeightTrucksOnBridge());
//    }
}
