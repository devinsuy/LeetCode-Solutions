class Solution:
    # Bottom up recursive
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Edge case
        if(len(nums) < 2):
            return len(nums)
        
        # Cache LIS beginning at a given index
        dp = [None] * len(nums)
        dp[-1] = 1
        globalMax = 1
        
        def LISUtil(i: int):
            # Read from cache
            if(dp[i]):
                return dp[i]
            
            currVal = nums[i]
            maxLIS = 1
            
            # Each value that is an increase from our current has a potentially
            # higher LIS than our running max
            for j in range(i+1, len(nums)):
                if(currVal < nums[j]):
                    maxLIS = max(maxLIS, 1 + LISUtil(j))
            
            # Cache results and update globalMax
            nonlocal globalMax 
            globalMax = max(globalMax, maxLIS)
            dp[i] = maxLIS
            return maxLIS
        
        # Generate LIS bottom up
        for i in range(len(nums)-2, -1, -1):
            LISUtil(i)
            
        return globalMax

    # Bottom up iterative
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Edge cases
        if(len(nums) < 2):
            return len(nums)
        
        globalMax = 1
        dp = [1] * len(nums)
        
        for i in range(len(nums)-2, -1, -1):
            currMax = 1
            currVal = nums[i]
            for j in range(i+1, len(nums)):
                if(currVal < nums[j]):
                    currMax = max(currMax, 1 + dp[j])
                    
            dp[i] = currMax
            globalMax = max(globalMax, currMax)
        
        return globalMax
        
        
        
            