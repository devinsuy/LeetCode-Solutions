from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Base cases
        if len(nums) == 1 or len(set(nums)) == 1: 
            return 1
        
        # Memoization, map index to the LIS at that position
        cache = {0 : 1}
        
        def lengthOfLIS_util(index: int) -> int:
            if index in cache: 
                return cache[index]

            # The max LIS at the current index is the max LIS
            # of all precending indexes + 1
            max_LIS = float('-inf')
            for i in range(index):
                if nums[i] < nums[index]:
                    # Lookup value from cache
                    if i in cache:
                        max_LIS = max(cache[i], max_LIS)
                    else:
                        max_LIS = max(lengthOfLIS_util(i), max_LIS)
            
            # If found, return the maximum LIS from the preceding 
            # subproblems + the addition of our current value
            if max_LIS == float('-inf'):
                max_LIS = 1
            else:
                max_LIS += 1
            cache[index] = max_LIS

            return max_LIS

        # Recursively generate the LIS for each index
        # keep a running global maximum
        global_max_LIS = float('-inf')
        for i in range(len(nums)):
            global_max_LIS = max(global_max_LIS, lengthOfLIS_util(i))
        
        print(cache)

        return global_max_LIS

# Expected: 4
nums = [10,9,2,5,3,7,101,18]


# Expected: 4
#nums = [0,1,0,3,2,3]

# Expected: 1
#nums = [7,7,7,7,7,7,7]

# Expected: 6
nums = [1,3,6,7,9,4,10,5,6]

s = Solution()
print(s.lengthOfLIS(nums))