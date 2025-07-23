// https://leetcode.com/problems/asteroid-collision/?envType=problem-list-v2&envId=stack

package Medium;
import java.util.LinkedList;
import java.util.List;

public class AsteroidCollision {

    public int[] asteroidCollision(int[] asteroids) {
        
        List<Integer> rem = new LinkedList<>();

        for(int asteroid: asteroids){
            while(!rem.isEmpty() && asteroid < 0 && rem.getFirst() > 0){
                int winner = asteroid + rem.getFirst();

                if(winner < 0){
                    rem.removeFirst();
                }
                else if(winner > 0){
                    asteroid = 0;
                }
                else{
                    rem.removeFirst();
                    asteroid = 0;
                }
            }
            if(asteroid != 0){
                rem.addFirst(asteroid);
            }
        }

        return rem.stream().mapToInt(i -> i).toArray();
    }

    

    public static void main(String[] args) {
        AsteroidCollision sol = new AsteroidCollision();

        int[] c = new int[] {5,10,-5};
        System.out.println(sol.asteroidCollision(c));
        
        c = new int[] {8,-8};
        System.out.println(sol.asteroidCollision(c));
        
        c = new int[] {10,2,-5};
        System.out.println(sol.asteroidCollision(c));

    }
}
