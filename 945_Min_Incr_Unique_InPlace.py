from collections import defaultdict

class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        # Edge cases
        if(A is None or len(A) < 2): 
            return 0
        
        A.sort()
        incrCount = 0
        seen = set([A[0]])
        
        # Build numbers in place for each conflict, number of increments is 
        # the difference to the closest possible value from the current value
        for i in range(1, len(A)):
            curr = A[i]
            if(curr in seen):                       # O(1) check if the value is distinct
                A[i] = A[i-1] + 1                   # The last value was distinct assign 1 + this value
                incrCount += (A[i] - curr)          # Calculate the number of increments needed to do so
                seen.add(A[i])
            else:
                seen.add(curr)
        
        return incrCount