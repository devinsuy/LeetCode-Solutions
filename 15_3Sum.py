class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Edge case
        if(len(nums) < 3):
            return []
        
        output = set([])
        nums.sort()   

        prevVal = None
        for i in range(len(nums)):
            if(nums[i] == prevVal):             # Do no reprocess duplicates (same triplets will be reached)
                continue
            
            # All value at i and all values to the right of i 
            # are positive since sorted, 0 sum is impossible
            if(nums[i] > 0):
                break
                        
            target = -nums[i]
            seen = set()
            for j in range(i+1, len(nums)):
                curr = nums[j]
                complement = target - curr
                
                # Hash sorted tuples to avoid duplicates
                if(complement in seen):
                    output.add(tuple(sorted([-target, curr, complement])))
                seen.add(curr)
                                
            prevVal = nums[i]
        
        return output
                           