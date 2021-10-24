import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class back_11729 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        System.out.println((int)Math.pow(2,N)-1);
        hanoi(N,1,3,2);

    }

    public static void hanoi(int N, int start, int to,int via){
        if(N==1){
            move(start, to);
        }
        else{
            hanoi(N-1,start,via,to);
            move(start, to);
            hanoi(N-1,via,to,start);
        }
    }
    public static void move(int start,int to){
        System.out.println(start+" "+to);
    }
}
