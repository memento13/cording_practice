import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class back_2789 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[] cards = new int[n];

//        카드삽입
        st = new StringTokenizer(br.readLine());
        for(int i=0;i<n;i++){
            cards[i] = Integer.parseInt(st.nextToken());
        }

//        최대한 m에 가까운 카드 3장의 합 찾아야함
        int max = 0;
        int mix = 0;
        for(int i=0;i<n-2;i++){
            for(int j=i+1;j<n-1;j++){
                for(int k=j+1;k<n;k++){
                    mix = cards[i]+cards[j]+cards[k];
                    if(mix<=m && mix>max){
                        max = mix;
                    }
                }
            }
        }
        System.out.println(max);


    }
}
