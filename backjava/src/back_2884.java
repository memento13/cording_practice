import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class back_2884 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int hour = Integer.parseInt(st.nextToken());
        int minute = Integer.parseInt(st.nextToken());

        int cal_minute = 60*hour + minute - 45;

        if(cal_minute<0){
            cal_minute = (24*60)+cal_minute;
        }

        System.out.println(cal_minute/60+" "+cal_minute%60);


    }
}
