package back;
import java.util.Scanner;
public class Back_2675 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		
		for(int i=0;i<N;i++) {
			int n = sc.nextInt();
			String str = sc.nextLine();
			
			String result = "";
			for(int j = 0;j<str.length();j++) {
				for(int k = 0;k<n;k++) {
					result += str.charAt(j);
				}
			}
			result = result.replaceAll(" ","");
			System.out.println(result);
		}
		sc.close();
	}

}
