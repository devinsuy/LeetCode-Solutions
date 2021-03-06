class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Edge case
        if(len(nums) < 3):
            return []
        
        # Set of sorted triplet tuples
        output = set([])
        
        # Fix the first value, the other two should sum to -nums[i] for all 3 to sum to 0
        for i in range(len(nums)-2):
            target = -nums[i]
            seen = set([nums[i+1]])
            
            # 2 sum excluding the first value
            for j in range(i+2, len(nums)):
                curr = nums[j]
                complement = target - curr
                if(complement in seen):
                    triplet = [-target, curr, complement]
                    triplet.sort()
                    output.add(tuple(triplet))                  # Sorted tuple will hash the same as any duplicates

                seen.add(curr)
        
        return output
                           
                