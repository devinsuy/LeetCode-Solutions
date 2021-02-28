from collections import defaultdict
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # Edge case
        if(len(time) < 2):
            return 0
    
        maxTime = max(time)
        timeIndex = defaultdict(list)           # Map each time to a list of indicies it appears at
        timeComps = defaultdict(set)            # Map each time to a list of its complement vals <= maxTime
        
        # Build index mapping
        for i, val in enumerate(time):
            timeIndex[val].append(i)
        
        # Build complement values that would make a valid pair 
        for val in time:
            comp = 60 - (val % 60)
            while(comp <= maxTime):
                if(comp in timeIndex):
                    timeComps[val].add(comp)
                comp += 60
        
        # Return the number of indices a value appears to the right of an index
        def validPairCount(leftIndex: int, val: int):
            indices = timeIndex[val]
            for i, index in enumerate(indices):
                if(index > leftIndex):
                    return len(indices) - i
            return 0
                
        # For each complement, increment by the amount of indices to the right 
        # of the given index that the complement appears at
        pairCount = 0
        for i, val in enumerate(time):
            for comp in timeComps[val]:
                if(comp in timeIndex):
                    pairCount += validPairCount(i, comp)
                    
        return pairCount
                    
        
        