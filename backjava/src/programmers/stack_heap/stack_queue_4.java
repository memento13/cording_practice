package programmers.stack_heap;

import java.util.LinkedList;
import java.util.List;

public class stack_queue_4 {
    public static void main(String[] args) {
        int[] prices =
                {1, 2, 3, 2, 3, 1};
//                {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
//                {1, 2, 3, 2, 3};
        int[] answer = {};

        /**
         * 주식객체를 받아서 등록순서, 가격과 지속시간(0)을 등록함
         * 매번 값을 읽을때마다 등록된 주식객체와 비교
         * 등록된 주식객체가 현재 값보다 낮으면 sustaintime+1후 answer[num]에 sustainTime 등록, 해당객체 answerList로 이동;
         * 등록된 주식객체가 현재 값보다 높으면 sustaintime+1
         * 마지막까지 다 읽으면 마지막 값 answer[num]에 sustainTime 등록
         */

        StockList stockList = new StockList();
        for(int i=0;i<prices.length;i++){
//            System.out.println("price : "+prices[i]);

            stockList.addStock(i,prices[i]);

//            answer = stockList.solution(prices.length);
//
//            for (int j : answer) {
//                System.out.print(" " + j);
//            }
//            System.out.println();
//            System.out.println("==============");
        }
        answer = stockList.solution(prices.length);

    }

}

class StockList{
    private List<Stock> stockList = null;
    private List<Stock> answerList = null;

    public StockList() {
        this.stockList = new LinkedList<>();
        this.answerList = new LinkedList<>();
    }

    public void moveStocktoAnswer(Stock stock){
        answerList.add(stock);
    }

    public void addStock(int num,int price){
        //이번 주식입력시 현재 값보다 구매시 값이 높은 경우의 주식들
        List<Stock> removeList = new LinkedList<>();
        for (Stock stock : stockList) {
            stock.sustain();
            if(!stock.brrrrrrrrrrr(price)){
                moveStocktoAnswer(stock);
                removeList.add(stock); //stockList에서 지워야하는 주식
            }
        }
        //모아놨다가 반복문이 끝난후 일괄적으로 지워버림
        for (Stock stock : removeList) {
            stockList.remove(stock);
        }
        Stock stock = new Stock(num,price);
        stockList.add(stock);
    }

    public int[] solution(int size){
        int[] result = new int[size];
        for (Stock stock : stockList) {
            result[stock.getNum()] = stock.getSustainTime();
        }
        for (Stock stock : answerList) {
            result[stock.getNum()] = stock.getSustainTime();
        }
        return result;
    }
}
class Stock{
    private int num;
    private int price;
    private int sustainTime;

    public Stock(int num, int price) {
        this.num = num;
        this.price = price;
        this.sustainTime = 0;
    }
    public void sustain(){
        this.sustainTime+=1;
    }
    public int getNum() {
        return num;
    }
    public int getPrice() {
        return price;
    }
    public int getSustainTime() {
        return sustainTime;
    }
    public boolean brrrrrrrrrrr(int price){
        if(this.getPrice()<=price){
            return true;
        }
        return false;
    }
}