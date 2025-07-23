// https://leetcode.com/problems/permutations/?envType=problem-list-v2&envId=backtracking
package Medium;

import java.util.List;
import java.util.ArrayList;

public class Permutations{

    List<List<Integer>> res = new ArrayList<>();
 
    public List<List<Integer>> permute(int[] nums){
        
        List<Integer> nums1 = new ArrayList<>();
        for(int num: nums){
            nums1.add(num);
        }
        backtrack(nums1, new ArrayList<>());
        return res;

    }

    /* Does not work */
    // private void backTrack(List<Integer> nums, List<Integer> path){

    //     if(nums.isEmpty()){
    //         res.add(new ArrayList<>(path));
    //         System.out.println(res);
    //         return;
    //     }

    //     for(int i=0; i < nums.size(); i++){
    //         List<Integer> subList = new ArrayList<>(nums.subList(0, i));
    //         subList.addAll(new ArrayList<>(nums.subList(i+1, nums.size())));
    //         System.out.println(subList);
    //         path = new ArrayList<>(path);
    //         path.add(nums.get(i));
    //         System.out.println(path);
    //         backTrack(subList, path);
    //     }
    // }

    private void backtrack(List<Integer> nums, List<Integer> path) {
        if (nums.isEmpty()) {
            res.add(new ArrayList<>(path));
            return;
        }

        for (int i = 0; i < nums.size(); i++) {
            List<Integer> remaining = new ArrayList<>(nums);
            List<Integer> newPath = new ArrayList<>(path);
            newPath.add(remaining.remove(i));
            backtrack(remaining, newPath);
        }
    }

    public static void main(String[] args) {
        Permutations perm = new Permutations();
        System.out.println(perm.permute(new int[]{1, 2, 3}));
        System.out.println(perm.permute(new int[]{0}));
    }

}