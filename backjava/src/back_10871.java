import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class back_10871 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());
        int num;

        st =  new StringTokenizer(br.readLine());
        for(int i=0;i<n;i++){
            num = Integer.parseInt(st.nextToken());
            if(num<x){
                System.out.print(num+" ");
            }
        }

    }
}
