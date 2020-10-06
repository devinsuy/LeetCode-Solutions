'''
Given an array nums of n integers where n > 1,  
return an array output such that output[i] is equal to 
the product of all the elements of nums except nums[i]
'''
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums is None or len(nums) == 0: return []
        elif len(nums) == 1: return nums 
        elif len(nums) == 2: return [nums[1], nums[0]]

        # Generate products from left to right
        l_prod = [None] * len(nums)
        l_prod[0] = curr_prod = nums[0]
        l_ptr = 1
        for num in nums[1:]:
            curr_prod *= num
            l_prod[l_ptr] = curr_prod
            l_ptr += 1
        
        # Generate products from right to left
        r_prod = [None] * len(nums)
        r_prod[-1] = curr_prod = nums[-1]
        r_ptr = len(nums) - 2
        for num in reversed(nums[:-1]):
            curr_prod *= num
            r_prod[r_ptr] = curr_prod
            r_ptr -= 1

        # Handle edge elements manually
        output = [None] * len(nums)
        output[0] = r_prod[1]
        output[len(nums)-1] = l_prod[len(nums)-2]
        
        for ptr in range(1, len(nums)-1):
            output[ptr] = l_prod[ptr-1] * r_prod[ptr+1]

        return output     


# Test Case: Expected [24,12,8,6]
nums = [1,2,3,4]
s = Solution()
print(s.productExceptSelf(nums))