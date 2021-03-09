class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Edge cases, assumption input of only positive numbers 
        if(not nums or target < 0):
            return 0
        
        # O(nlogn) to sort values into ascending order
        nums.sort()
        
        # Map value -> to the number of ways to sum to target from that value
        cache = {}
        
        def combSumUtil(val: int) -> int:
            # Base cases
            if(val > target):
                return 0
            if(val == target):
                return 1
            if(val in cache):
                return cache[val]
            
            # Expand all possible combination branches from the current value
            numCombos = 0
            for complement in nums:
                if(val + complement > target):
                    break
                numCombos += combSumUtil(val + complement)
                
            cache[val] = numCombos
            return numCombos
        
        
        # Build dp cache top down, calculating number of possible
        # combinations beginning from each value
        totalCombos = 0
        for val in nums[::-1]:
            totalCombos += combSumUtil(val)
                
        return totalCombos
            
            
            