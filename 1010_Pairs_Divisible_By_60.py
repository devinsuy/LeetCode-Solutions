from collections import defaultdict
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # Edge case
        if(len(time) < 2):
            return 0
        
        # Map each mod 60 remainder to the number of values that generate this remainder
        remainCount = defaultdict(int)
        pairCount = 0
        
        # Increment pairCount by the amount of previously seen values that have 
        # a remainder equal to the desired complement, update count for curr remainder
        for val in time:
            if(val % 60 == 0):
                remainder = comp = 0
            else:
                remainder = val % 60
                comp = 60 - remainder
                
            pairCount += remainCount[comp]
            remainCount[remainder] += 1
                    
        return pairCount
                    
        
        