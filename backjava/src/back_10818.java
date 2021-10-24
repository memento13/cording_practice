import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class back_10818 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        ArrayList<Integer> arr = new ArrayList<>();
        while(st.hasMoreTokens()){
            arr.add(Integer.parseInt(st.nextToken()));
        }
        br.close();
        System.out.println(Collections.min(arr)+" "+Collections.max(arr));
    }
}
