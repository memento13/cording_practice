package programmers.greedy;

public class greedy_3 {
    public static void main(String[] args) {

        class Solution {
            public String solution(String number, int k) {
                StringBuilder numberSb = new StringBuilder(number);
                int length;
                int i;
                int j;
                boolean flag;

                for(i=0;i<k;i++){
                    flag = true;
                    length = numberSb.length();
                    for(j=0;j<length-1;j++){
//                        Integer first = numberSb.charAt(j)-'0';
                        Integer first = (int)numberSb.charAt(j);
                        if(first==9){
                            continue;
                        }
                        Integer second = (int)numberSb.charAt(j+1);
                        //뒷자리보다 앞자리가 작은 수인경우
                        if(second>first){
                            numberSb.deleteCharAt(j);
                            flag = false;
                            break;
                        }
                    }
                    //모든 숫자가 내림차순인경우
                    if(flag){
                        int temp = k - i;
                        return numberSb.substring(0,length-temp);
                    }
                }

                return numberSb.toString();
            }
        }

        String number = "54321";
        int k = 2;
        Solution solution = new Solution();
        System.out.println(solution.solution(number, k));

    }


}


/*
StringBuilder numberSb = new StringBuilder(number);
                int temp;
                int i;
                int j;

                for(i=0;i<k;i++){
                    int length = numberSb.length();
                    temp = length-1;
                    for(j=0;j<length-1;j++){
                        if(numberSb.charAt(j)<numberSb.charAt(j+1)){
                            temp = j;
                            break;
                        }
                    }
                    numberSb.deleteCharAt(temp);
                }

                return numberSb.toString();
 */