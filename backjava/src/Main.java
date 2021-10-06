import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int origin = Integer.parseInt(br.readLine());
        int tmp = origin;
        int cnt = 0;
        int a,b,c,d; // "a"+"b"="c"+"b"
        while (true){

            a=tmp/10;
            b=tmp%10;
            c=(a+b)/10;
            d=(a+b)%10;
            tmp = b*10 +d;
            cnt++;
            if(tmp==origin){
                break;
            }
        }
        System.out.println(cnt);
    }
}
