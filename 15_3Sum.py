class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Edge case
        if(len(nums) < 3):
            return []
        
        output = []
        nums.sort()   

        prevVal = None
        for i in range(len(nums)):
            # Do no reprocess duplicates (same triplets will be reached)
            if(nums[i] == prevVal):
                continue
            
            # All value at i and all values to the right of i 
            # are positive since sorted, 0 sum is impossible
            if(nums[i] > 0):
                break
                        
            # Track duplicates remaining array to avoid duplicate triplets
            prevLeft = prevRight = None
            
            target = -nums[i]
            left = i+1
            right = len(nums) - 1
            
            # 2 sum with remaining array, avoiding duplicate repairings
            while(left < right):
                # Do not consider adjacent repeating values (array is sorted)
                if(nums[left] == prevLeft): 
                    left += 1
                    continue
                if(nums[right] == prevRight):
                    right -= 1
                    continue
                currSum = nums[left] + nums[right]
                
                # Triplet found, increment/decrement both pointers
                if(currSum == target):
                    output.append([-target, nums[left], nums[right]])
                    prevLeft = nums[left]
                    prevRight = nums[right]
                    left += 1
                    right -= 1

                # Sum is too large, decrement right pointer to decrease sum next pass (since sorted)
                elif(currSum > target):
                    prevRight = nums[right]
                    right -= 1    
                
                # Sum is too small, increment left pointer to increase sum next pass
                else:
                    prevLeft = nums[left]
                    left += 1
                    
            prevVal = nums[i]
        
        return output
                           