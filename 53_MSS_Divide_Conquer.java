class Solution {
    public int maxCrossSum(int[] nums, int left, int right){
        int mid = left + ((right-left) / 2);
        int leftMax, rightMax, curr;
        leftMax = rightMax = Integer.MIN_VALUE;
        
        // Find the max left sum moving from mid to left
        curr = 0;
        for(int i = mid; i > -1; i--){
            curr += nums[i];
            if(curr > leftMax) leftMax = curr;
        }
        // Find the max right sum moving from mid+1 to right
        curr = 0;
        for(int i = mid+1; i < nums.length; i++){
            curr += nums[i];
            if(curr > rightMax) rightMax = curr;
        }
        return leftMax + rightMax;
        
    }
    public int MSS(int[] nums, int left, int right){
        // Base case, single element reached
        if(left == right)
            return nums[left];
        int mid = left + ((right-left) / 2);
        
        int lMSS = this.MSS(nums, left, mid);
        int rMSS = this.MSS(nums, mid+1, right);
        int crossMax = this.maxCrossSum(nums, left, right);
        
        // The MSS is the max of the cross sum, left mss and right mss
        return Math.max(Math.max(lMSS, rMSS), crossMax);
    }
    
    public int maxSubArray(int[] nums) {
        return this.MSS(nums, 0, nums.length-1);
    }
}