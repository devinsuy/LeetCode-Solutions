
class Solution:
    # O(n) Time and O(1) space
    def missingNumber(self, nums: List[int]) -> int:
        if nums == None or len(nums) == 0:
            return -1

        
        # Calculate the expected sum of the list if it wasn't missing a number
        expected_sum = actual_sum = 0
        for num in range(1, len(nums)+1): # O(n)
            expected_sum += num
        expected_sum += (num for num in nums)

        # Iterate through our list and find the actual sum
        for num in nums: # O(n)
            actual_sum += num
        
        return expected_sum - actual_sum
