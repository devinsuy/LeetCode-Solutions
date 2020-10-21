from typing import List 

class Solution:
    # def trap(self, height: List[int]) -> int:
    #     left = between = start = water = 0

    #     while left < len(height):                                   # Increase the left by one until we reach the end (we might not find a value greater than the current left)
    #         for i in range(left+1, len(height)):
    #             left_val = height[left]
    #             val = height[i]

    #             if val >= left_val:     
    #                 if between != 0:                                # We found an end point, water lies between
    #                     min_height = min(left_val, val)
    #                     curr_water = between * min_height
    #                     for j in range(left+1, i):                  # Subtract the displacement
    #                         curr_water -= height[j]
    #                     water += curr_water
    #                     print("water found")
    #                 left = i
    #                 between = 0
    #             else:
    #                 between += 1
            
    #         between = 0
    #         left += 1
        
    #     return water

    def trap(self, height: List[int]) -> int:
        # Set the maximum height for each index moving left to right
        min_heights = [None] * len(height)
        l_ptr = 0
        r_ptr = len(height) - 1
        left_max = right_max = float('-inf')

        # First obtain the max height associated with each index moving left to right
        for curr_height in height:
            if curr_height > left_max:
                left_max = curr_height
            min_heights[l_ptr] = left_max
            l_ptr += 1
        
        # Repeat right to left, keep the minimum of the two
        for curr_height in reversed(height):
            if curr_height > right_max:
                right_max = curr_height
            min_heights[r_ptr] = min(min_heights[r_ptr], right_max)
            r_ptr -= 1

        # Water is equal to the height at the index minus and displacement (height)
        water = 0
        for i, height in enumerate(height):
            water += (min_heights[i] - height)
        
        return water
        







a = [0,1,0,2,1,0,1,3,2,1,2,1]
a = [4,2,3]
s = Solution()
print(s.trap(a))