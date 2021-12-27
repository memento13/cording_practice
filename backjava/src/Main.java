import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigDecimal;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int[] arr;
//        ArrayList<Integer> arr = new ArrayList<>();

//        n입력
        int n = Integer.parseInt(br.readLine());
        arr = new int[n];
        st = new StringTokenizer(br.readLine());
//        xi 입력
        for(int i=0;i<n;i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        int[] clone = arr.clone();
        Arrays.sort(clone);
//         map으로 검색 최적화
        Map<Integer, Integer> rank = new HashMap<>();
        int index = 0;
        for(int i : clone){
            if(!rank.containsKey(i)){
                rank.put(i,index);
                index++;
            }
        }


//        입력받은 xi값을 rank를 참조하여 인덱스 값을 출력함
        StringBuilder sb = new StringBuilder();
        for(int i : arr){
            sb.append(rank.get(i));
            sb.append(" ");
        }
        System.out.println(sb);
    }
}