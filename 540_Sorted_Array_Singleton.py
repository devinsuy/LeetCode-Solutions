'''
Input: SORTED array where each element appears twice except one
Output: The value of the singleton element

Constraints: O(logn) Time, O(1) space

- Must discard half input on each pass
- Recursively generate soluton
- Min element is at a[0], max element is at a[-1]


'''

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # Edge case, singleton list
        if(len(nums) == 1):
            return nums[0]
        
        def singleUtil(left: int, right: int) -> int:
            size = right - left + 1
            
            # Base case, singleton found
            if(size == 1):
                return nums[left]
            
            # Determine whether the mid element pairs to the left or right
            mid = int((left+right) / 2)
            matchLeft = nums[mid-1] == nums[mid]
            matchRight = nums[mid+1] == nums[mid]
            
            # Base case, mid element is the singleton
            if(not matchLeft and not matchRight):
                return nums[mid]
            
            # Base case, return the unmatched element 
            if(size == 3):
                if(matchLeft):
                    return nums[mid+1]
                else:
                    return nums[mid-1]
            
            # Calculate the size and bounds of the left and right
            # subarrays after removing the mid element and its pair
            if(matchLeft):
                lRight = mid-2                      # Right bound of left subarray (inclusive)
                rLeft = mid+1                       # Left bound of right subarray (inclusive)
            else:
                lRight = mid-1
                rLeft = mid + 2
            sizeLeft = lRight - left + 1
            sizeRight = right - rLeft + 1
                
            # The singleton MUST lie in the subarray with the odd size
            if(sizeLeft % 2 == 1):
                return singleUtil(left, lRight)     # Recurse left
            else:
                return singleUtil(rLeft, right)     # Recurse right
        
        
        # Recursively find singleton
        return singleUtil(0, len(nums)-1)
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        