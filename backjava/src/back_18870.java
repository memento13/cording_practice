import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class back_18870 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        ArrayList<Integer> arr = new ArrayList<>();

//        n입력
        int n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
//        xi 입력
        for(int i=0;i<n;i++){
            arr.add(Integer.parseInt(st.nextToken()));
        }

//        set으로 중복제거후 list로 변환하여 정렬후 인덱스를 내보냄
        Set<Integer> removeDuplicatesSet = new HashSet<>(arr);
        ArrayList<Integer> rank = new ArrayList<>(removeDuplicatesSet);
        Collections.sort(rank);

//        입력받은 xi값을 rank를 참조하여 인덱스 값을 출력함
        StringBuffer sb = new StringBuffer();
        for(int i=0;i<n;i++){
            sb.append(rank.indexOf(arr.get(i)));
            sb.append(" ");
        }
        System.out.println(sb);
    }

}
