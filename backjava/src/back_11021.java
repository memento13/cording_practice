import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class back_11021 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int result;
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());

        for(int i = 1; i<=T;i++){
            st = new StringTokenizer(br.readLine()," ");
            result = Integer.parseInt(st.nextToken())+Integer.parseInt(st.nextToken());
            System.out.println("Case #"+i+": "+result);
        }
        br.close();
    }
}
