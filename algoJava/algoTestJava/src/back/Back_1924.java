package back;

import java.util.Calendar;
import java.util.Scanner;

public class Back_1924 {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int x = s.nextInt();
		int y = s.nextInt();
		
		Calendar c = Calendar.getInstance();
		c.set(2007,x-1,y);
		
		int temp = c.get(Calendar.DAY_OF_WEEK);
		
		String[] week = {"SUN", "MON","TUE","WED","THU","FRI","SAT"};
		System.out.println(week[temp-1]);

		s.close();

	}
}
