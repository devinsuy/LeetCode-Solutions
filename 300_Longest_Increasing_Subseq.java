// - Order remains the same
// - Numbers can be excluded (not the same as a subarray)
// - If a number(s) are not increasing skip them, so long as there are increasing
// numbers further right in the array the subsequence can continue

// Brute force:
//  Begin a subsequence at each index
//  iterate through each number from left ot right, increment increaseCount each time a larger number than the current is found
//  Return the maximum length found

 
class Solution {
    public int lengthOfLIS(int[] nums) {
        // Edge cases
        if(nums == null)
            return 0;
        if(nums.length <= 1)
            return nums.length;
        
        // Use dynamic approach where index corresponds to the max length
        // increasing subsequence up to that index
        int[] dp = new int[nums.length];
        for(int i = 0; i < dp.length; i++) dp[i] = 1;
        int currLen;
        
        // For each number, check value against each number to the left of it 
        for(int i = 1; i < nums.length; i++){
            for(int j = 0; j < i; j++){
                // If a previous number is less than the current, the longest increasing
                // subseq at the current index i is 1 + the longest at the previous index j
                // since we "add" this number to our subsequence
                if(nums[i] > nums[j]){
                    currLen = 1 + dp[j];
                    dp[i] = Math.max(currLen, dp[i]);
                }
            }
        }  
        int maxLen = 1;
        for(int seqLen : dp)
            if(seqLen > maxLen)
                maxLen = seqLen;
        
        return maxLen;
    }
}