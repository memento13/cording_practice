import java.io.BufferedReader;
import java.io.InputStreamReader;

class Main {

    public static void main(String[] args) throws Exception {
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