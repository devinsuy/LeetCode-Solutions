from collections import defaultdict

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # Edge cases
        if(nums is None or len(nums) == 1):
            return 0
        
        pairCount = 0     
        numCount = defaultdict(int)
        for num in nums: numCount[num] += 1
        
        used = set([])
        for num in nums:
            # The number was previously processed, avoid duplicates
            if(num in used): continue
            complement = num + k
            
            # The number and complement are the same, there must atleast 
            # be 2 of them in the list
            if(num == complement):
                if(numCount[num] > 1):
                    pairCount += 1
                    used.add(num)
            else:
                if(complement in numCount):
                    pairCount += 1
                    used.add(num)
                    
        return pairCount
                
                