class Solution {
    // Time Complexity: O(n)
    // Space Complexity: O(1)
    public int[] productExceptSelf(int[] nums) {
        int[] out = new int[nums.length];
        out[0] = 1;
        
        // Generate output excluding self moving left to right
        for(int i = 1; i < nums.length; i++){
            out[i] = out[i-1] * nums[i-1];
        }
        
        // Use accumulating variable to generate output excluding self
        // from right to left (right only accumulates after passing the index)
        int right = 1;
        for(int i = nums.length-1; i > -1; i--){
            out[i] *= right;
            right *= nums[i];
        }
        
        return out;
    }
}