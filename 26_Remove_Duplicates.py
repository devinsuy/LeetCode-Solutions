class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0

        # Use two pointer approach for single pass O(n)
        # we lock in an element at the index if it is distinct 
        i = 0
        for j in range(1,len(nums)):
            if nums[j] != nums[i]:          # We have located a new distinct value
                i += 1                      # Store it at one index from our last distinct
                nums[i] = nums[j]
        
        # We don't care about the end part of the array after our distinct values

        return i + 1                        # The length of the array

