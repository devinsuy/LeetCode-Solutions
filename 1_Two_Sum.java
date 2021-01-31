import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> seen = new HashMap<Integer, Integer>();
        seen.put(nums[0], 0);
        int curr, complement;
        
        for(int i = 1; i < nums.length; i++){
            curr = nums[i];
            complement = target - curr;
            
            // Complement exists in list, return the saved index and current
            if(seen.containsKey(complement)){
                return new int[] {i, seen.get(complement)};
            }
            seen.put(curr, i);
        }
        
        // Valid solution does not exist
        return null;
    }
}