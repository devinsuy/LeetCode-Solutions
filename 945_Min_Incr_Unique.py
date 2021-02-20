from collections import defaultdict

class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        # Edge cases
        if(A is None or len(A) == 0): 
            return 0
        
        # List is already unique
        if(len(set(A)) == len(A)):
            return 0
        
        # Map each value to its frequency in the list, locate the max value
        freqMap = defaultdict(int)
        for num in A: freqMap[num] += 1
            
        # Determine max value, and find any missing values in the list
        A.sort()        
        maxVal = A[-1]
        minVal = A[0]
        numSet = set(A)
        missingVals = []
        for val in range(maxVal-1, minVal, -1):
            if(val not in numSet): missingVals.append(val)
            
        # Get the smallest number > currVal that isn't in the list
        # otherwise this value is 1 past the current maximum value
        def getReplaceVal(currVal: int) -> int:
            nonlocal maxVal 
            nonlocal missingVals
            if(missingVals):
                for i in range(len(missingVals)-1, -1, -1):
                    num = missingVals[i]
                    if(num > currVal):
                        return missingVals.pop(i)
                    
            maxVal += 1
            return maxVal
            
        # Iterate, the incrCount from a given value is the difference
        # from the non unique value to the next closest value it can assume
        incrCount = 0
        for i in range(len(A)):
            currNum = A[i]
            if(freqMap[currNum] > 1):
                replaceVal = getReplaceVal(currNum)
                incrCount += (replaceVal - currNum)
                freqMap[currNum] -= 1
        
        return incrCount