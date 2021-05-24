class Solution {
    public int maxSubArray(int[] nums) {
        // Edge case
        if(nums.length == 1)
            return nums[0];
        
        int n = nums.length - 1;
        int[] dp = new int[n+1];
        int maxSum = dp[n] = nums[n];
        
        // Track max possible sum at each index
        int curr;
        for(int i = n-1; i >= 0; i--){
            curr = nums[i];
            dp[i] = Math.max(curr, curr+dp[i+1]);
            maxSum = Math.max(maxSum, dp[i]);
        }
        return maxSum;
    }
}