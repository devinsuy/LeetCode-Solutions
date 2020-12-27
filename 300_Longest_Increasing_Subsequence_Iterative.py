from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = [0] * len(nums)
        cache[0] = global_max_ILS = 1

        # Iteratively generate the ILS for each index
        for i in range(1, len(nums)):
            max_ILS = 0
            max_val = nums[i]       

            # Locate the maximum ILS preceding our index
            for j in range(0, i):
                if nums[j] < max_val:
                    max_ILS = max(max_ILS, cache[j]) 

            # The max ILS at this index is the maximum
            # of all preceding indices now including our current
            cache[i] = max_ILS + 1
            global_max_ILS = max(global_max_ILS, cache[i])
        
        return global_max_ILS






# Expected: 4
nums = [10,9,2,5,3,7,101,18]


# Expected: 4
#nums = [0,1,0,3,2,3]

# Expected: 1
#nums = [7,7,7,7,7,7,7]

# Expected: 6
#nums = [1,3,6,7,9,4,10,5,6]

s = Solution()
print(s.lengthOfLIS(nums))