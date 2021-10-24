import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class back_1436 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int cnt = 0;
        int num = 665;
        while (true){
            if(String.valueOf(num).contains("666")){
                cnt++;
            }
            if(cnt==n){
                break;
            }
            num++;
        }
        System.out.println(num);
    }
}
