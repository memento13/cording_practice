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
                    System.out.println(entry.getKey()+" : "+genresPlaysSortedByPlay);
                    searchGenre = entry.getKey();
                    break;
                }
            }
            if(searchGenre==null){
                System.out.println("없음");
                break;
            }
            System.out.println("searchGenre = " + searchGenre);
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
            System.out.println("songsByGenre = " + songsByGenre);
            Collections.sort(songsByGenre);

//            플레이수로 정렬
            List<Integer> playsBySong = new ArrayList<>(playsMap.values());
            Collections.sort(playsBySong,Collections.reverseOrder());
            System.out.println("playsBySong = " + playsBySong);

            int i=0;
            for (Integer play : playsBySong) {
                if(i>1){
                    break;
                }
                i++;
                for (Integer song : songsByGenre) {
                    if(playsMap.get(song)==play && !songRank.containsValue(song)){
                        songRank.put(rank,song);
                        rank++;
                        break;
                    }
                }
            }
        }
        System.out.println("songRank = " + songRank);

        answer = new int[songRank.size()];
        for(int i=0;i<songRank.size();i++){
            answer[i]=songRank.get(i);
        }
        for (int i : answer) {
            System.out.println("i = " + i);
        }


    }
}
