from typing import List, Set
from copy import deepcopy

class Solution:
    # Each gene is the same length, 8 characters long
    def checkDiff(self, s1: str, s2: str):
        diffCount = 0
        for i in range(8):
            if s1[i] != s2[i]:
                diffCount += 1
        return diffCount
    
    
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:

        def mutateUtil(seen: Set[str], curr: str, mutCount: int) -> int:
            # Goal mutation reached
            if(curr == end):
                return mutCount
            
            # Avoid repeating mutations
            seen.add(curr)
            
            # Mutations are only allowed to change 1 character at most each pass
            nextMutations = []
            for mutation in bank:
                if(mutation not in seen and self.checkDiff(curr, mutation) == 1): 
                    nextMutations.append(mutation)
                    
            # No valid mutations from this point forward
            if(len(nextMutations) == 0):
                return -1
            
            # Expand each valid next mutation
            minMutations = float('inf')
            for mutation in nextMutations:
                currCount = mutateUtil(deepcopy(seen), mutation, mutCount+1)
                if(currCount != -1 and currCount < minMutations):
                    minMutations = currCount
            
            # No valid paths were found
            if(minMutations == float('inf')):
                return -1
            
            return minMutations
        
        
        return mutateUtil(set([]), start, 0)