class Solution {
    public int maxProduct(int[] nums){
        // Base case
        if(nums.length == 1)
            return nums[0];
        
        // Keep a running min and running max, these two can quickly
        // flip if a negative number is encountered, use a global max
        int globalMax, currMax, currMin, minProd, maxProd, num;
        globalMax = currMin = currMax = nums[0];        
        
        for(int i = 1; i < nums.length; i++){
            num = nums[i];
            
            // Multiplication by zero resets running max and min a new subarray must 
            // be started, all subarrays including the 0 will have product 0
            if(num == 0){              
                currMin = currMax = 1;
                if(globalMax < 0) globalMax = 0;
                continue;  
            }
            
            // Generate the next 2 products by applying the current number to the
            // 2 running values, reassign them accordingly in case they flip
            minProd = currMin * num;
            maxProd = currMax * num;
            currMin = Math.min(num, Math.min(minProd, maxProd));
            currMax = Math.max(num, Math.max(minProd, maxProd));
            
            // Update global maximum value seen
            if(currMax > globalMax) 
                globalMax = currMax;
        }
        
        return globalMax;
    }
}