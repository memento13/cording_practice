package programmers.greedy;

public class greedy_3 {
    public static void main(String[] args) {

        class Solution {
            public String solution(String number, int k) {
                StringBuffer numberSb = new StringBuffer(number);
                for(int i=0;i<k;i++){
                    boolean flag = true;
                    int length = numberSb.length();
                    for(int j=0;j<length-1;j++){
                        Integer first = numberSb.charAt(j)-'0';
                        if(first==9){
                            continue;
                        }
                        Integer second = numberSb.charAt(j+1)-'0';
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

