package back;
import java.util.Scanner;

public class Back_1032 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner s = new Scanner(System.in);
		int N = s.nextInt();
		StringBuilder filename = new StringBuilder(s.next());
		for(int i = 1;i<N;i++) {
			StringBuilder input = new StringBuilder(s.next());
			
			for(int j=0;j<filename.length();j++) {
				if(input.charAt(j)!=filename.charAt(j)) {
					filename.setCharAt(j,'?');
				}
			}
		}
		System.out.println(filename);
		s.close();

	}

}
