from typing import List
class Solution:
    def avg_two(self, a: int, b: int):
        return (a+b)/2

    def get_median(self, nums: List[int]):
        mid_index = int(len(nums) / 2)
        if len(nums) % 2 == 0:
            return self.avg_two(nums[mid_index], nums[mid_index-1])
        else:
            return nums[mid_index]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        median_1 = self.get_median(nums1)
        median_2 = self.get_median(nums2)
        
        return round(self.avg_two(median_1, median_2))



s = Solution()

# Expected: 14
a = [1,7,13,18]
b = [8,15,22,27]

s.findMedianSortedArrays(a,b)
