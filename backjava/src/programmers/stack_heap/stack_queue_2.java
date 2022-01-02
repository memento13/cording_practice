package programmers.stack_heap;

import java.util.LinkedList;
import java.util.Queue;

public class stack_queue_2 {

    public static void main(String[] args) {
        int[] priorities =
//                {2, 1, 3, 2};
                {1, 1, 9, 1, 1, 1};
        int location =
//                2;
                0;
        int answer = 0;

        /**
         * Document(문서) 객체는 num(문서번호),priority(중요도)를 가진다
         * 1. 큐를 이용하여 DocumentQueue를 만든다.
         * 2.큐에 문서객체들을 집어넣는다
         * 3. 큐에서 문서를 poll 하여 현재 큐에서 poll한 문서보다 높은 중요도가 있는지 확인한다.
         * 4. 큐에서 poll한 문서보다 높은 중요도가 있다면 poll한 문서를 다시 add한다.
         * 5. poll한 문서가 제일 높은 중요도를 가지고 있다면 그대로 두고 answer에 1을 더한다.
         *      ㄴ poll한 문서의 num이 location과 같다면 answer를 반환하고 종료한다.
         *          ㄴ 아니라면 3부터 반복 한다.
         */

        DocumentQueue documentQueue = new DocumentQueue(priorities);

        while (true){
            Document document = documentQueue.isPoll();
            if(document!=null){
                answer++;
                if(document.getNum()==location){
                    break;
                }
            }
        }

        System.out.println("answer = " + answer);
    }


}

class Document{
    private int num;
    private int priority;

    public Document(int num, int priority) {
        this.num = num;
        this.priority = priority;
    }

    public int getNum() {
        return num;
    }

    public int getPriority() {
        return priority;
    }
}

class DocumentQueue{
    private Queue<Document> documentQueue;

    public DocumentQueue(int[] priorities) {
        this.documentQueue = new LinkedList<>();
        int num=0;
        for (int priority : priorities) {
            documentQueue.add(new Document(num++,priority));
        }
    }

    public Document isPoll(){
        Document pollDocument = documentQueue.poll();
        if(checkDocumentIsMaxPriorityInQueue(pollDocument)){
            return pollDocument;
        }
        else {
            documentQueue.add(pollDocument);
            return null;
        }
    }

    public boolean checkDocumentIsMaxPriorityInQueue(Document document){
        for (Document queDoc : documentQueue) {
            if(document.getPriority()<queDoc.getPriority()){
                return false;
            }
        }
        return true;
    }
}