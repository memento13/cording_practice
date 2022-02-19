package programmers.bruteforce;

import java.util.HashSet;
import java.util.Set;

public class BruteForce_2 {
    public static void main(String[] args) {
        String numbers = "17";
        int answer = 0;

        PrimeNumbersFinder primeNumbersFinder = new PrimeNumbersFinder(numbers);


        primeNumbersFinder.finder("",numbers);

        answer = primeNumbersFinder.getResult();

        System.out.println("answer = " + answer);
    }
}
class PrimeNumbersFinder{
    String numbers;
    Set<Integer> numberSet;

    public PrimeNumbersFinder(String numbers) {
        this.numbers = numbers;
        this.numberSet = new HashSet<>();
    }

    void finder(String now, String numbersWithOutNow ){
        if(!now.equals("")){
            int nowInt = Integer.parseInt(now);
            numberSet.add(nowInt);
        }

        for(int i=0;i<numbersWithOutNow.length();i++){
            finder(now+numbersWithOutNow.charAt(i),numbersWithOutNow.substring(0,i)+numbersWithOutNow.substring(i+1));
        }

    }

    int getResult(){
        int result = 0;
        for (Integer number : numberSet) {
            if(isPrime(number)){
                result++;
            }
        }
        return result;
    }

    boolean isPrime(Integer number){
        if(number<=1){
            return false;
        }
        for(int i =2; i<=Math.sqrt(number);i++){
            if(number%i==0){
                return false;
            }
        }
        return true;
    }

}