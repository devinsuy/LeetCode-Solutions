# Input: Integer array
# Output: The maximum continguous sum in the array

# Assumptions:
#   - Sum of a given subarray (i,n) must use all values a[i] .. a[n]
#   - Problem can be solved using divide and conquer
#   - How many subarrays an array with n elements have?


# Kadanes algorithm O(n)
class Solution:
    def maxSubArray(self, nums):
        max_sum = float('-inf')
        current_sum = 0

        for i in range(len(nums)):
            # Determine whether to add the current element to the previous subarray
            # or start a new subarray with just the current element
            current_sum = max(current_sum + nums[i], nums[i])
            if current_sum > max_sum:
                max_sum = current_sum           # Update pointer

        return max_sum 


# Divide and conquer O(nlogn)
class Solution:
    # Subarray of a cross-sum must contain the middle element 
    # returns max_sum[left:mid+1] + max_sum[mid+1:right+1]
    def cross_sum(self, nums, left, right):
        mid = left + ((right - left) // 2)
        
        # Calculate max cross sum for left half
        left_max_sum = float('-inf')
        current_sum = 0
        for i in range(mid, left-1, -1):
            current_sum += nums[i]
            if current_sum > left_max_sum:
                left_max_sum = current_sum

        # Calculate max cross sum for right half
        right_max_sum = float('-inf')
        current_sum = 0
        
        for i in range(mid+1, right+1, 1):
            current_sum += nums[i]
            if current_sum > right_max_sum:
                right_max_sum = current_sum

        return left_max_sum + right_max_sum

    
    def mss_util(self, nums, left, right):
        # Base case
        if left == right:
            return nums[left]

        mid = left + ((right - left) // 2)

        # Recursive calls
        left_sum = self.mss_util(nums, left, mid)
        right_sum = self.mss_util(nums, mid+1, right)
        cross_sum = self.cross_sum(nums, left, right)

        return max([left_sum, right_sum, cross_sum])


    def maxSubArray(self, nums):
        # Validation cases
        if nums is None or len(nums) == 0:
            return None

        return self.mss_util(nums, left=0, right=len(nums) - 1)