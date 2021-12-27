import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class back_14888 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        List<Integer> arr = new ArrayList<>();

        st = new StringTokenizer(br.readLine());
        while(st.hasMoreTokens()){
            arr.add(Integer.parseInt(st.nextToken()));
        }

        List<Integer> operators = new ArrayList<>();

        st = new StringTokenizer(br.readLine());
        int operator = 0;
        while(st.hasMoreTokens()){
            for(int i=0;i< Integer.parseInt(st.nextToken());i++){
                operators.add(operator);
            }
            operator++;
        }

        int n;
        int tmp=0;
        if(tmp==0){

        }
        else if(tmp==1){

        }
        else if(tmp==2){

        }
        else if(tmp==3){

        }







    }
}
