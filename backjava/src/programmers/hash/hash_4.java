package programmers.hash;

import java.util.*;

public class hash_4 {
    public static void main(String[] args) {
        String[] genres = {"classic", "pop", "classic", "classic", "pop"};
        int[] plays = {500, 600, 150, 800, 2500};
        int[] answer = {};
        int songCnt = plays.length;
        Map<Integer,String> genresMap = new HashMap<>();
        Map<Integer,Integer> playsMap = new HashMap<>();
        Map<String,Integer> genresPlays = new HashMap<>();
        Map<Integer,Integer> songRank = new HashMap<>();
        for(int i=0;i<songCnt;i++){
            genresMap.put(i,genres[i]);
            playsMap.put(i,plays[i]);
            if(!genresPlays.containsKey(genres[i])){
                genresPlays.put(genres[i],plays[i]);
            }
            else {
                genresPlays.put(genres[i],genresPlays.get(genres[i])+plays[i]);
            }
        }
        List<Integer> genresPlaysSortedByPlays = new ArrayList<>(genresPlays.values());
        Collections.sort(genresPlaysSortedByPlays,Collections.reverseOrder());


        String searchGenre = null;
        int rank=0;

        for (Integer genresPlaysSortedByPlay : genresPlaysSortedByPlays) {
            for (Map.Entry<String, Integer> entry : genresPlays.entrySet()) {
                if(entry.getValue()==genresPlaysSortedByPlay){

                    searchGenre = entry.getKey();
                    break;
                }
            }
            if(searchGenre==null){
                break;
            }

            /**
             * 장르값으로 해당 장르 노래 고유번호 찾기
             * 고유번호로 정렬
             * 플레이수로 정렬
             * 고유번호와 랭크를 songRank 에 고유번호,랭크로 저장
             */

//            장르값으로 해당 장르 노래 고유번호 찾기
            List<Integer> songsByGenre = new ArrayList<>();
            for (Integer song : genresMap.keySet()) {
                if(genresMap.get(song).equals(searchGenre)){//동일장르인 경우
                    songsByGenre.add(song);
                }
            }

            Collections.sort(songsByGenre);

//            플레이수로 정렬
            List<Integer> playsBySong = new ArrayList<>(playsMap.values());
            Collections.sort(playsBySong,Collections.reverseOrder());


            int i=0;
            for (Integer play : playsBySong) {
                if(i>1){
                    break;
                }

                for (Integer song : songsByGenre) {
                    if(playsMap.get(song)==play && !songRank.containsValue(song)){
                        songRank.put(rank,song);
                        rank++;
                        i++;
                        break;
                    }
                }
            }
        }


        answer = new int[songRank.size()];
        for(int i=0;i<songRank.size();i++){
            answer[i]=songRank.get(i);
        }


    }
}
